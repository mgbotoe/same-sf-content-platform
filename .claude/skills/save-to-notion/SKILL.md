---
name: save-to-notion
description: Save generated SAME SF content (posts, campaigns, calendars) to Notion. Auto-invoked when user says "save to notion", "push to notion", "add to notion", "update notion", or "notion calendar".
---

# Save to Notion

Push generated SAME SF content to the existing Notion Communications Hub and Content Calendar.

## Existing Notion Structure

The SAME SF Communications Hub already exists in Notion. Do NOT create new databases.

### Content Calendar Database
- **Database URL**: `https://www.notion.so/e711f5af58c24d7ebfe8d577c06b10e1`
- **Data Source ID**: `4b828522-e96b-4eed-9424-7b5298a485a1`
- **Parent page**: SAME SF Communications Hub (`2d5d7843-d866-813a-81f7-de88b12c7231`)

### Content Calendar Schema (use these exact property names)

```sql
"Post Title" TEXT           -- title field (required)
"Status" TEXT               -- one of: "Idea", "Drafting", "Review", "Scheduled", "Posted"
"Platform" TEXT             -- one of: "LinkedIn", "Newsletter", "Both"
"Content Type" TEXT         -- one of: "Event Announcement", "Event Recap", "Member Spotlight",
                            --         "Sponsor Feature", "Observance", "Thought Leadership",
                            --         "Newsletter", "Engagement"
"Theme" TEXT                -- one of: "Military & Service", "Public-Private Collab",
                            --         "DEI & Leadership", "Technical Excellence", "STEM Outreach"
"Audience" TEXT             -- JSON array, zero or more of: "Members", "Sponsors", "DoD", "Students", "General"
"date:Publish Date:start"   -- ISO-8601 date string (e.g., "2026-03-05")
"date:Publish Date:end"     -- NULL for single dates
"date:Publish Date:is_datetime" -- 0 for date, 1 for datetime
"Draft" TEXT                -- Full post text
"Hashtags" TEXT             -- Hashtag string (e.g., "#SAMESF #AECCommunity")
"Post URL" TEXT             -- LinkedIn post URL (after publishing)
"Engagement" FLOAT          -- Engagement rate (after publishing)
"Notes" TEXT                -- Graphic needs, tagging instructions, timing notes
"Alt Version" TEXT          -- Alternative version of the post
```

### Other Notion Pages (for reference)

| Page | ID | Purpose |
|---|---|---|
| Communications Hub | `2d5d7843-d866-813a-81f7-de88b12c7231` | Main hub page |
| Example Posts | `b75c01d7760d4312a8e6f40d10549975` | Library of proven content |
| SOPs | `2d5d7843-d866-81e4-aa7a-cc30f28770e2` | Step-by-step procedures |
| Visual Assets | `2d5d7843-d866-8115-a9b3-d38dc4cbca0f` | Logos, colors, templates |
| Voice Analysis | `2d5d7843-d866-8115-b983-d14e61f73f33` | Patterns from 82-post analysis |

## Before Saving

1. **Confirm content is finalized** — ask the user if the content is approved before saving
2. **Determine what to save**: Individual post, campaign sequence, or monthly calendar
3. **Load Notion tools**: Use ToolSearch for `+notion create` to load the MCP tools

## Saving an Individual Post

Use `mcp__claude_ai_Notion__notion-create-pages` with:

```json
{
  "parent": {"data_source_id": "4b828522-e96b-4eed-9424-7b5298a485a1"},
  "pages": [{
    "properties": {
      "Post Title": "[First line or topic]",
      "Status": "Drafting",
      "Platform": "LinkedIn",
      "Content Type": "[matching type]",
      "Theme": "[matching theme]",
      "Audience": "[\"General\"]",
      "Draft": "[Full post text]",
      "Hashtags": "#SAMESF [+ others]",
      "Notes": "[Graphic description, tagging instructions]",
      "date:Publish Date:start": "2026-MM-DD",
      "date:Publish Date:is_datetime": 0
    }
  }]
}
```

## Saving a Campaign Sequence

Create multiple pages in one call — one for each post in the sequence:

```json
{
  "parent": {"data_source_id": "4b828522-e96b-4eed-9424-7b5298a485a1"},
  "pages": [
    {"properties": {"Post Title": "Post 1: Save the Date", ...}},
    {"properties": {"Post Title": "Post 2: Sponsor Reveal", ...}},
    {"properties": {"Post Title": "Post 3: Early Bird Reminder", ...}}
  ]
}
```

Add a note in each post's Notes field indicating the campaign name and sequence position (e.g., "Golf Tournament 2026 Campaign - Post 3 of 8").

## Saving a Monthly Calendar

Create all planned posts as "Idea" status entries with scheduled dates.

## Updating Post Status

Use `mcp__claude_ai_Notion__notion-update-page` to update:
- Status: "Drafting" → "Review" → "Scheduled" → "Posted"
- Post URL: Add the LinkedIn URL after publishing
- Engagement: Add metrics after publishing

## Content Type Mapping

Map generated content to the correct Content Type:

| Skill Used | Content Type |
|---|---|
| `/linkedin-sequence` (event promo) | Event Announcement |
| `/event-recap` | Event Recap |
| `/member-spotlight` | Member Spotlight |
| `/member-spotlight` (sponsor) | Sponsor Feature |
| `/military-holiday` | Observance |
| `/throwback` | Thought Leadership |
| `/email-campaign` | Newsletter |
| `/content-calendar` (polls, etc.) | Engagement |

## After Saving

Confirm to the user:
- What was saved (post titles, count)
- Status set (Drafting/Idea/Scheduled)
- Notion link to the Content Calendar for review
- Any remaining content that needs to be generated
