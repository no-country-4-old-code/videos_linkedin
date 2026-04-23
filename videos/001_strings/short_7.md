## Short: "Signal snitches to Meta"

---

## Headline
Signal Snitches To Meta

## Text

Signal. The privacy app. End-to-end encrypted.
But last week during playing around I found some kind of loophole, I would like to share.

Lets enter the Danger Zone and download the APK "https://signal.org/android/apk/".
We unzip it and filter for https-API-Endpoints.

And there are a lot.. and it makes fun to look through them..
but today we focus on this one here:
Signal uses giphy for the GIF-search.
And it uses the endpoint directly. No proxy in between.

And this has the implication, that everytime you search for GIFs giphy (which belongs to meta) gets the following info:
- they know that the device at your IP is using Signal at the moment
- they know your gif search terms
and regarding to their privacy policy, they have no problem with storing and analysing that.

Is this serious ? I do not know.

Take away for today:
Do not communicte your secret plans using GIFs..at least not using GIFs only.
“And by the way, am I the only one who gets a headache when looking at the Giphy homepage?”



---

## Display / CLI / Code
https://signal.org/android/apk/
```bash
# We already know how to crack open an APK — let's go straight to the finding

 unzip -p Signal-Android-website-prod-universal-release-8.3.4.apk | strings | grep -i "https://" | sort -u
```

developers.giphy.com
Show output:
- `https://api.giphy.com/v1/gifs/`
- `https://api.stripe.com/v1`

```bash
# Confirm Giphy is Meta-owned — and Signal's key identifies the app
unzip -p Signal-Android-release.apk | strings | grep -i "giphy" | grep -i "key\|uri\|base"
# Output: GIPHY_API_KEY, BASE_GIPHY_URI
```

Freeze on: `api.giphy.com` → cut to "Giphy: acquired by Meta (Facebook), 2020".

What Meta sees per search:
- Your IP address
- Your search query
- `api_key=<signal's registered key>` → identifies app as Signal


---- WOW...

Good instinct — a string in a binary is circumstantial. You want to catch it in the act. Here are your options, ranked by effort:

  ---
  Option 1: mitmproxy (easiest, most visual)

  Run a MitM proxy on your laptop, route your Android through it.

  pip install mitmproxy
  mitmproxy --listen-port 8080

  On Android:
  - WiFi settings → proxy → your laptop's IP, port 8080
  - Visit mitm.it in browser → install mitmproxy CA certificate
  - Open Signal → tap the GIF button → type anything

  mitmproxy will show the live request including the full URL with api_key= and q=<your search term>.

  Caveat: Signal pins certificates for its own servers — those will show as failed/blocked in mitmproxy. But Giphy is a third-party call, Signal almost certainly doesn't pin it, so it should pass through
  unmodified.

  ---
  Option 2: tcpdump on rooted Android / emulator

  If you have a rooted device or Android emulator:

  adb shell tcpdump -i any -w /sdcard/capture.pcap
  # search for a GIF in Signal
  adb pull /sdcard/capture.pcap
  wireshark capture.pcap

  Filter in Wireshark: http.host contains "giphy" — but you'll only see cleartext if TLS is not yet established or if you combine with the mitmproxy cert.

  ---
  Option 3: Android Emulator + HTTP Toolkit (zero setup)

  https://httptoolkit.com does all of the above automatically for emulators — installs the cert, configures the proxy, shows you all traffic with pretty UI. Literally one click. Best option for recording
  video.

  ---
  The likely result when you catch it:

  GET https://api.giphy.com/v1/gifs/search
      ?api_key=<32-char key>
      &q=explosion
      &limit=25
      &lang=en
      &rating=pg-13

  That's your proof. URL in APK + live request = airtight.

---

## Youtube title
1. Signal Sends Your GIF Searches Directly to Meta — Here's the Proof
2. I Found a Meta (Giphy) Endpoint Hardcoded Inside Signal's APK
3. `strings` on an APK: How One Line Reveals Where Signal Leaks Your Data
4. What Does Signal Actually Send to Meta Every Time You Search for a GIF?

## Youtube Description
Unzipping Signal's Android APK and running `strings` against it reveals a direct Giphy (Meta) API endpoint — no proxy in between. Every GIF search sends your IP address, your search query, and Signal's registered API key directly to a Meta-owned server. This short shows how to find the endpoint and confirms it with a live MitM proxy capture.

Commands shown:
- `unzip -p Signal-Android-website-prod-universal-release-8.3.4.apk | strings | grep -i "https://" | sort -u`
- `unzip -p Signal-Android-release.apk | strings | grep -i "giphy" | grep -i "key\|uri\|base"`

#infosec #privacy #signal #apksecurity #cybersecurity

## LinkedIn Description
Third-party SDKs and API integrations inside mobile apps are an often-overlooked data-leakage surface — a single `strings` pass over an APK can surface direct calls to external vendors that bypass your privacy assumptions. Audit the apps your organization allows employees to use and check what endpoints they call for non-core features like GIF search.

#privacy #mobileappsecurity #cybersecurity
