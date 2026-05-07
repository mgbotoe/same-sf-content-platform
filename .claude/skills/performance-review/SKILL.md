---
name: performance-review
description: Analyze recent SAME SF LinkedIn post performance, identify top content, and recommend reposts or variants. Auto-invoked when user says "performance review", "how are posts doing", "analyze posts", "what's working", "top posts", or "recommend reposts".
---

# Performance Review

Analyze SAME SF LinkedIn post performance and recommend reposts, variants, or strategy adjustments.

## Before Analyzing

1. **Read these files**:
   - `data/brand-voice.md` — posting frequency benchmarks
   - `data/content-themes.md` — content mix targets

2. **Get the data**: Ask the user for one of:
   - A LinkedIn content export file (.xls/.xlsx)
   - OR access to the Notion Content Calendar (fetch via MCP)
   - OR specific post metrics they want to review

## Analysis Framework

### 1. Frequency Audit
- Posts per week over the review period
- Compare against target: 1-2/week baseline, max 3/week campaigns, 12/month cap
- Flag any weeks with 0 posts (gaps) or 4+ posts (over-posting)
- Flag any same-day double posts

### 2. Engagement Analysis
- Average engagement rate vs. benchmark (4-8% for pages with 1K-5K followers)
- Top 5 posts by engagement rate
- Bottom 5 posts by engagement rate
- Engagement by day of week (compare to Tue-Fri recommendation)
- Engagement by content type

### 3. Content Mix Check
- Actual mix vs. target: 60% value / 25% thought leadership / 15% promotional
- Are recaps and spotlights getting enough share? (They're the highest-ROI content)
- Any content types over- or under-represented?

### 4. Pattern Recognition
- Which Voice Analysis formulas are being used? (Meaning+Moment+Community, Scene+Purpose+Gratitude, etc.)
- Are opening lines hooks or labels?
- Comment rate (target: 0.3%+ of impressions)
- Are posts ending with genuine questions?

## Output Format

```
## SAME SF Performance Review: [Date Range]

### Summary
- Total posts: [N]
- Average engagement rate: [X]% (benchmark: 4-8%)
- Posts per week average: [X] (target: 1-2 baseline)

### Top 5 Performers
[Table: date, title snippet, engagement, impressions, content type]

### Bottom 5 Performers
[Table: same format]

### What's Working
- [Specific patterns from top performers]

### What's Not Working
- [Specific patterns from low performers]

### Content Mix Actual vs. Target
[Table comparing actual percentages to 60/25/15 target]

### Recommendations
1. [Specific actionable recommendation]
2. [Repost/variant suggestions for top performers]
3. [Frequency or timing adjustments]
4. [Content type shifts]
```

## Repost Recommendations

For top-performing posts, suggest:
- **Repost timing**: Wait 2-4 weeks minimum
- **New angle**: Same topic, different hook or format
- **Format upgrade**: Text post → carousel, single image → multi-image
- **Quote extraction**: Pull a quote card from a long-form post

## Variant Suggestions

For high-engagement content types, propose:
- **Series extension**: "This spotlight format worked — here are 3 more members to feature"
- **Cross-format**: "This recap performed well as text — create a carousel version"
- **Follow-up**: "This scholarship post drove engagement — do a follow-up with student quotes"

## After Analyzing

Offer to:
1. Generate content variants via the appropriate skill
2. Update the content calendar in Notion via `/save-to-notion`
3. Plan next month's content based on findings via `/content-calendar`
