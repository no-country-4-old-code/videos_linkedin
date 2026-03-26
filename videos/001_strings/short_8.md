## Short: "Your Photos Are Snitching"

---

## Headline
Your Photos Are Snitching

## Text

Every photo you take is a confession.

Camera model. Lens. GPS coordinates. Exact timestamp down to the second.
All baked silently into the file. All invisible to the naked eye.

Your grandma just posted a selfie from her "secret" vacation spot.
exiftool told me she's at 48.8566° N, 2.3522° E.
That's Paris. Hi grandma.

Stripping it is one command. Faking it is also one command.
That photo "taken in Berlin"? Shot in a basement in Cleveland.
exiftool doesn't judge.

Now — LinkedIn, X, Instagram, they all strip EXIF on upload. Automatically. To protect their users.
So your grandma's Paris selfie is safe on social media.

But most of the time the same images are posted on multiple plattforms.
So searching the first appearence of the image via a reversed image search (TinEye), might lead to an unstripped image.

Also some webpages are not stripping apart info : https://www.trump.com/leadership/donald-j-trump-biography .
And boy is this image talkitive.. create at .. edited with photoshop .. here the whole history .. and the old filename was "xyz" - wow..
here was a professional. I know putting binaries under version control might bloat.. but before I do this naming ? 

But the photo she sent you directly over email? WhatsApp? USB stick?
Full metadata. Still there. Still talking.

Know what's in your files before someone else does it for you.

---
## Info about Trump picture

  ---
  The Basics
  - File: donald-j-trump.jpg — 980x1282px, 1.1 MB, only 1.3 megapixels. Potato quality for a president.
  - User Comment: Screenshot — So this whole elaborate retouched image... started as a screenshot.

  The Software Trail — It's Complicated
  - Created in Adobe Lightroom 6.4 on Macintosh — but then bounced through Adobe Photoshop 24.6 (also Mac) no less than 10 times before being saved back to
  Lightroom. Someone was really committed.
  - The History Action field has saved appearing 7 times. Every "final" save apparently needed 6 more final saves.

  The Raw File Name (Best Part)
  Raw File Name: Trump Retouched copy 2.jpg
  "copy 2" — there was a copy 1 that apparently wasn't good enough. And who knows how many non-copy versions came before.

  The Timeline
  - Original capture: 2023-07-21 at 13:49:29 (UTC-5) — a Friday afternoon
  - Final save: 15:48:56 — nearly 2 hours of retouching a screenshot of Trump

  AI Masking Data
  - There's a Lightroom AI mask (Mask 1 + Mask 1 Inverted) with thousands of brush dab coordinates embedded in the file — Lightroom tracked every single
  brushstroke used for selective editing. The mask reference point is 0.751918, 0.378906 — roughly the upper-right quadrant. Touching up the hair? Almost
  certainly.

  The Irony
  - Brightness: +50, Contrast: +25 — someone literally brightened and boosted contrast on a Trump photo. Make it pop.
  - White Balance: As Shot — at least they left the orange tone as-is.
  - Measurement Flare: 0.999% — nearly 1% lens flare. Even the metadata is dramatic.

  Profile Creator: Hewlett-Packard — the color profile embedded is the ancient sRGB IEC61966-2.1 from 1998, created by HP. It's older than most of Trump's
  controversies.


---

## Display / CLI / Code

```bash
# Install
sudo apt install libimage-exiftool-perl

# Read everything out of a photo
exiftool photo.jpg
```

Show output flood:
- `GPS Latitude  : 48.8566 N`
- `GPS Longitude : 2.3522 E`
- `Date/Time Original : 2026:03:15 14:32:07`
- `Camera Model Name : iPhone 15 Pro`
- `Software : 17.3.1`

```bash
# Nuke all metadata — one flag
exiftool -all= photo.jpg

# Verify it's gone
exiftool photo.jpg
# Output: (nothing interesting left)
```

```bash
# Plant fake GPS and timestamp
exiftool \
  -GPSLatitude="52.5200" \
  -GPSLatitudeRef="N" \
  -GPSLongitude="13.4050" \
  -GPSLongitudeRef="E" \
  -DateTimeOriginal="2026:01:01 08:00:00" \
  photo.jpg

exiftool photo.jpg | grep -E "GPS|Date"
# GPS Latitude  : 52.5200 N   <- Berlin
# Date/Time Original : 2026:01:01 08:00:00
```
