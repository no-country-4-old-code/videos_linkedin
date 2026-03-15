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
Shorts are additional videos tied to the same topic as the main video. They are **<= 1 minute** each. Up to 4 per main video. Same structure as script.md.

## Script File Format

Each `script.md` (and `short_*.md`) must have two separate sections:

```
## Text
(spoken words only)

## Display / CLI / Code
(all screen actions, commands, code snippets)
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
| `[short]` | **Create shorts**: Create up to 4 short video scripts (`short_1.md` to `short_4.md`) in the video folder. Each short touches the topic of the main `script.md` but is self-contained and <= 1 minute. Set status to `[o]` when done. |
| `[o]` | Ignore — already in progress or done. |
| `[r]` | Ignore. |
| `[x]` | Ignore. |
| `[yyyy.mm.dd]` | Ignore — published. |
