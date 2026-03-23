# Project Instructions for Claude

## Repository Structure

```
videos/          - One subfolder per video. Each folder contains script.md and optionally short_*.md files.
ideas_raw/       - Raw ideas. Do not create files here.
status.md        - Tracks the status of all videos. Always check this before starting work.
```

## Video Format

Each video has two phases:
1. **On-camera intro** (1-2 sentences): Hook the audience.
2. **Screen recording** (CLI / code / repos): The main content. Voice-over only, no face visible.
3. **On-camera outro**: Wrap up and tease the next video.

Videos are max 5 minutes, information-dense, and entertaining. Show short, exciting things.

### Shorts
Shorts are additional videos tied to the same topic as the main video. They are **<= 1 minute** each. Up to 4 per main video. Same structure as script.md. Each short must cover a distinct angle — no overlapping content between shorts.

## Script File Format

Each `script.md` (and `short_*.md`) must have two separate sections:

```
## Text
(spoken words only)

## Display / CLI / Code
(all screen actions, commands, code snippets)
```

For `short_*.md` files, add a `## Headline` section before `## Text`. The headline is a catchy, punchy title of **4–5 words max** used as the video title on social media.

```
## Short: "..."

---

## Headline
Four Or Five Words

## Text
...

## Display / CLI / Code
...
```

## Style Guidelines

- Match the tone and style of existing scripts (direct, humorous, security-focused).
- All CLI / code examples must be real and working.
- No git commands — ever.

## Workflow: Status Codes in status.md

Read `status.md` and act based on the status of each video:

| Status | Action |
|--------|--------|
| `[ ]` | **Create**: Make a new folder under `videos/` and write a short description of what the video could be about. |
| `[s]` | **Write script**: Based on the description in the video folder, create `script.md` with `## Text` and `## Display / CLI / Code` sections combined. Set status to `[o]` when done. Match the repo's style. |
| `[c]` | **Rework script**: Split the existing script into separate `## Text` and `## Display / CLI / Code` sections (see format above). Set status to `[o]` when done. |
| `[short]` | **Create shorts**: Create up to 4 short video scripts (`short_1.md` to `short_4.md`) in the video folder. Each short touches the topic of the main `script.md` but is self-contained and <= 1 minute. Then create entry image layout HTML files (see below). Set status to `[o]` when done. |
| `[o]` | Ignore — already in progress or done. |

## Entry Image Layout HTML

After creating shorts, create one `entry_image_short_N.html` file per short inside `videos/<id>/material/shorts/`. Use `entry_image_short_N.html` where N matches the short number.

Each file shows **6 layout variants** of the short's headline as a 9:16 thumbnail (360×640px). Rules:

- **Black background** (`#000`) — no background image. Makes PNG export trivial.
- **Text in the upper half only** (top 320px). Lower half is reserved for a person overlay added in post.
- `overflow: hidden` on the title area — text must never escape the upper half.
- **Font sizing**: available width is 304px (360 - 28px padding each side). Estimate character width as `chars × 0.62 × font-size`. The longest word must fit within 304px (or 288px for sidebar variants that consume extra left padding). Reduce font size until it fits.
- **Colors**: use technical/hacker palette — matrix green `#00FF41`, electric blue `#4A9EFF`, deep red `#CC0000`, muted blue `#415D96`. No brand orange.
- No background image, no `backdrop-filter` blur.

### 6 variant styles

1. **Bold** — large stacked words, accent color on last word.
2. **Card** — dark card (`#0a0a0a`) with colored left border, label above words.
3. **Outline + filled** — outline stroked words mixed with solid-color filled words.
4. **Sidebar bar** — thin vertical colored bar on the left, words stacked to the right.
5. **Full-width band** — solid color band spanning full width, white text inside.
6. **Ghost text** — faint oversized text in background, normal-sized headline in foreground with glow.

Use `entry_image_short_1.html` in `videos/001_strings/material/shorts/` as the reference implementation.
| `[r]` | Ignore. |
| `[x]` | Ignore. |
| `[yyyy.mm.dd]` | Ignore — published. |
