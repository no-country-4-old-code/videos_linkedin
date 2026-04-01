## Short: "Your Photos Are Snitching"

---

## Headline
Metadata of Donald Trump

## Text

Nearly every image contains metadata in the exchangeable image format (EXIF).

Thankfully big social media platforms like Facebook, LinkedIn etc. strip most of the spicy metadata like original timestamps or geoposition from your uploaded images.

But in case of other websites it depends.

I want to share with you a very great image, no maybe the greatest image I stumbled upon during a lazy evening.
Let's download it and extract the metadata using the very great exiftool.

And we get a lot of metadata.
Filename, orignal timestamps -  Someone spent 2 hours retouching this one.
We can also see what the actions and which tools were used when.
Here Adobe Photoshop and Adobe Lightroom on a MAC.

The raw file name was "Trump Retouched copy 2.jpg".
Professional version handling - I like this.

And then.. it gets even more interesting.
Because we see that the editor applied a mask.
We cannot undo the masking, but I vibe coded a Python script which just plots green dots at those coordinates.
Here is the result.
They seemed to just eliminated some ugly clouds here.

But hey, we know when this image was updated.
Lets check what was on the webpage before.
We can do this with the Wayback Machine - the incarnation of the "the-internet-never-forgets"-phrase.
We select a screenshot in the early 2023.
https://www.trump.com/leadership/donald-j-trump-biography
https://web.archive.org/web/20230807055338/https://www.trump.com/leadership/donald-j-trump-biography
Lets download the old image as well and place them side by side.

Do you know those children's games where you see two images and need to spot the differences?
For a starter.. you might notice there is no sky in this one.
Also Mr. Trump forgot his pen here.
I do not know if this is a hint to a greater conspiracy going on, and to be honest, I do not care.
But I sincerely hope that you learned something about metadata in your images today.
If you send them around via Email or WhatsApp, they are not stripped of their metadata automatically.
And besides this...if you spot anymore differences let me know in the comments :)


---
## What to do

- Title the picture and "The Metadata of Donald Trump".
Show image Trump X account.
Switch to Trumps Webpage , go to his profile , download the file.
Show command line and use EXIFTOOL -> pipe to less
--> Mark filename, timestamps, history action, mask
- show python script
- show retouched_overlay
- Open Browser at Wayback machine and open page on januar 2023
- Download image
- Place them side by side  


## Info about Trump picture

  ---
  The Basics
  - File: donald-j-trump.jpg — 980x1282px, 1.1 MB, only 1.3 megapixels. Potato quality for a president.
  - User Comment: Screenshot — So this whole elaborate retouched image... started as a screenshot.

  The Software Trail — It's Complicated
  - Created in Adobe Lightroom 6.4 on Macintosh — but then bounced through Adobe Photoshop 24.6 (also Mac) no less than 10 times before being saved back to Lightroom. Someone was really committed.
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

```bash
# Extract brush dab coordinates from Lightroom mask data
exiftool -"Mask*Dabs" donald-j-trump.jpg | grep -oP "d \K[0-9.]+ [0-9.]+" > dabs.txt
wc -l dabs.txt
# 1519 dabs.txt
```

```python
# plot_dabs.py — yellow dots on the photo
from PIL import Image, ImageDraw
img = Image.open("donald-j-trump.jpg")
draw = ImageDraw.Draw(img)
for line in open("dabs.txt"):
    x, y = float(line.split()[0]), float(line.split()[1])
    draw.ellipse([x*980-2, y*1282-2, x*980+2, y*1282+2], fill="yellow")
img.save("retouched_overlay.jpg")
```

```bash
python3 plot_dabs.py
```

Show: side-by-side or zoom into hair area of `retouched_overlay.jpg` — dense cluster of yellow dots across the hairline.
