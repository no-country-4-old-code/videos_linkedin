## Short: "Your Photos Are Talking Behind Your Back"

---

## Text

Your photos contain more than just pixels.

Every time you post a selfie online, you might be sending your home address with it.
Because JPEG files store metadata. And strings just... reads it out loud.

Camera model. Software version. GPS coordinates. Timestamps.
One command. Zero effort.

Your phone has been narrating your life this whole time.
You just never listened.

Next time you post a photo online... maybe check what it's saying about you first.

---

## Display / CLI / Code

```bash
# Download or use any photo from your phone
strings photo.jpg | head -40
```

Show output highlighting:
- GPS coordinates (GPSLatitude, GPSLongitude)
- Camera model (e.g. "iPhone 15 Pro" or "Samsung SM-G998B")
- Software version (e.g. "iOS 17.1")
- Timestamp fields
- Possibly serial/device identifiers
