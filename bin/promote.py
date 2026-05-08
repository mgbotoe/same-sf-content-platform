#!/usr/bin/env python3
"""
Promote daily logs into long-term memory for the SAMESF marketing agent.

Single Anthropic API call. No claude.exe, no MCP servers.

Usage:
    python promote.py
    python promote.py --dry-run
    python promote.py --days 7
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import date, datetime, timedelta
from pathlib import Path

from anthropic import Anthropic

MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 4096
DEFAULT_DAYS = 3
AGENT_NAME = "SAMESF (Sage)"

COLD_FILES = ["campaigns.md", "decisions.md", "people.md", "preferences.md"]


def read_recent_logs(logs_dir: Path, days: int) -> str:
    if not logs_dir.exists():
        return ""
    cutoff = date.today() - timedelta(days=days)
    chunks = []
    for f in sorted(logs_dir.glob("*.md")):
        try:
            d = datetime.strptime(f.stem, "%Y-%m-%d").date()
        except ValueError:
            continue
        if d < cutoff:
            continue
        chunks.append(f"### {f.name}\n{f.read_text(encoding='utf-8', errors='replace')}")
    return "\n\n".join(chunks)


def read_memory(repo_root: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    hot = repo_root / "identity" / "memory.md"
    if hot.exists():
        out["identity/memory.md"] = hot.read_text(encoding="utf-8", errors="replace")
    cold_dir = repo_root / "memory"
    for name in COLD_FILES:
        path = cold_dir / name
        if path.exists():
            out[f"memory/{name}"] = path.read_text(encoding="utf-8", errors="replace")
    return out


PROMPT_TEMPLATE = """You are curating long-term memory for {agent_name}, a marketing agent.

Your job: read recent daily logs and current memory, produce structured updates.

# Memory architecture
- Hot (`identity/memory.md`): always loaded. Keep under 2500 tokens. Only essentials.
- Cold (`memory/*.md`): searched on demand. Detailed context.
  - `campaigns.md` — campaign history, performance notes
  - `decisions.md` — key decisions with rationale
  - `people.md` — people/stakeholder context
  - `preferences.md` — recurring patterns, brand voice notes

# Curation rules
1. Collapse runs of near-identical Session Log entries.
2. Drop older entries on different days that say the same thing — keep the most recent.
3. Don't collapse distinct facts together.
4. Hot memory must stay under 2500 tokens. Suggest archive moves if over.
5. Don't duplicate cold-memory entries — consolidate with existing.

# Output format
Respond with ONLY valid JSON, no prose. Schema:
{{
  "session_log_entry": "string or null — one-liner for ## Session Log in identity/memory.md, format '- [YYYY-MM-DD] <what>'. Null if no signal.",
  "hot_memory_replacement": "string or null — full replacement text for identity/memory.md if curation requires it. Null = no change.",
  "cold_updates": {{"memory/filename.md": "full replacement content or null"}},
  "summary": "string — 2-4 line report of what was promoted/collapsed/skipped"
}}

# Current memory
{memory_dump}

# Recent daily logs ({days} days)
{logs}

Return JSON only.
"""


def build_prompt(memory: dict[str, str], logs: str, days: int) -> str:
    memory_dump = "\n\n".join(f"## {name}\n```\n{content}\n```" for name, content in memory.items())
    return PROMPT_TEMPLATE.format(
        agent_name=AGENT_NAME,
        memory_dump=memory_dump or "(no memory files yet)",
        logs=logs or "(no recent logs)",
        days=days,
    )


def call_claude(prompt: str) -> dict:
    client = Anthropic()
    resp = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        messages=[{"role": "user", "content": prompt}],
    )
    text = "".join(block.text for block in resp.content if block.type == "text").strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
        if text.startswith("json\n"):
            text = text[5:]
    return json.loads(text)


def apply_updates(repo_root: Path, result: dict, dry_run: bool) -> list[str]:
    actions: list[str] = []
    hot_replacement = result.get("hot_memory_replacement")
    if hot_replacement:
        path = repo_root / "identity" / "memory.md"
        actions.append(f"replace identity/memory.md ({len(hot_replacement)} chars)")
        if not dry_run:
            path.write_text(hot_replacement, encoding="utf-8")
    elif entry := result.get("session_log_entry"):
        path = repo_root / "identity" / "memory.md"
        if path.exists():
            actions.append("append session log entry to identity/memory.md")
            if not dry_run:
                content = path.read_text(encoding="utf-8")
                if "## Session Log" in content:
                    content = content.rstrip() + "\n" + entry.rstrip() + "\n"
                else:
                    content = content.rstrip() + "\n\n## Session Log\n" + entry.rstrip() + "\n"
                path.write_text(content, encoding="utf-8")
    for rel_path, body in (result.get("cold_updates") or {}).items():
        if body is None:
            continue
        path = repo_root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        actions.append(f"replace {rel_path} ({len(body)} chars)")
        if not dry_run:
            path.write_text(body, encoding="utf-8")
    return actions


def write_runtime_marker(repo_root: Path) -> None:
    runtime = repo_root / ".claude" / "runtime"
    runtime.mkdir(parents=True, exist_ok=True)
    (runtime / "promote-last-run.ts").write_text(str(int(time.time())), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Promote SAMESF daily logs into memory.")
    parser.add_argument("--days", type=int, default=DEFAULT_DAYS)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--repo-root", default=os.environ.get("REPO_ROOT", str(Path(__file__).resolve().parent.parent)))
    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        return 2

    repo_root = Path(args.repo_root)
    if not repo_root.exists():
        print(f"ERROR: repo root not found: {repo_root}", file=sys.stderr)
        return 2

    logs = read_recent_logs(repo_root / "daily-logs", args.days)
    if not logs.strip():
        print(f"no daily logs in last {args.days} days — skipping")
        write_runtime_marker(repo_root)
        return 0

    memory = read_memory(repo_root)
    prompt = build_prompt(memory, logs, args.days)

    print(f"calling Claude (model={MODEL}, prompt={len(prompt)} chars)")
    try:
        result = call_claude(prompt)
    except json.JSONDecodeError as e:
        print(f"ERROR: model returned non-JSON: {e}", file=sys.stderr)
        return 3

    actions = apply_updates(repo_root, result, args.dry_run)
    print(f"summary: {result.get('summary', '(none)')}")
    print(f"actions ({'DRY RUN' if args.dry_run else 'applied'}):")
    for a in actions:
        print(f"  - {a}")

    if not args.dry_run:
        write_runtime_marker(repo_root)
    return 0


if __name__ == "__main__":
    sys.exit(main())
