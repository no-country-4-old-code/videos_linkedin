## Short: "Signal snitches to Meta - double check"

---

## Headline
Signal Snitches To Meta

## Text

Last time I claimed that Signal is sending your GIF request directly to Meta.
So every time you use a GIF, Meta knows that the device with your IP uses Signal at this moment in time.

But just finding the URL in the APK is more a hint than a proof.
I was a little bit sloppy here. 
So today let's go this extra mile.

I downloaded the android sdk and created a virtual android device on which I installed signal.
I also opened Wireshark on the hosting system and filtered for HTTP CONNECT requests to "api.giphy.com"
(filter for http.proxy_connect_host == "api.giphy.com")

When I enter the chat to send GIFs, we see that Wireshark detected calls from Signal going directly to Giphy.

Point proven.

---



## Display / CLI / Code

# Recap — the hint from last time
strings Signal-Android-release.apk | grep -i "giphy"
# Output: GIPHY_API_KEY, BASE_GIPHY_URI, https://api.giphy.com/v1/gifs/

# Today — the proof
# Step 1: install Signal on the Android emulator
adb install Signal-Android-release.apk

# Step 2: Wireshark on the host — apply filter
http.proxy_connect_host == "api.giphy.com"

# Step 3: open Signal → any chat → tap GIF → type anything
# → Wireshark captures:
CONNECT api.giphy.com:443 HTTP/1.1
Host: api.giphy.com:443

Freeze on Wireshark row → "Signal called home to Giphy (Meta)".

---

## Youtube title
1. I Caught Signal Calling Giphy (Meta) Live With Wireshark — Full Proof
2. String in an APK Was a Hint. This Wireshark Capture Is the Proof.
3. Verifying With Network Traffic: Signal Really Does Talk to Meta's Giphy
4. From APK String to Live Capture: How to Actually Confirm a Privacy Leak

## Youtube Description
Finding a third-party URL in an APK binary is circumstantial — a Wireshark capture is the actual proof. This short shows how to install Signal on an Android emulator, apply a `http.proxy_connect_host` filter in Wireshark on the host, and capture the live TLS CONNECT to `api.giphy.com` the moment you open Signal's GIF search.

Commands shown:
- `strings Signal-Android-release.apk | grep -i "giphy"`
- `adb install Signal-Android-release.apk`
- Wireshark filter: `http.proxy_connect_host == "api.giphy.com"`

#infosec #privacy #wireshark #networksecurity #cybersecurity

## LinkedIn Description
When assessing a privacy claim, strings-in-a-binary is evidence; live network capture is proof — and Wireshark on an emulator host makes that verification trivial. Combine static analysis of shipped artifacts with dynamic network monitoring to turn "potential" findings into confirmed incidents before they reach a report.

#blueteam #infosec #cybersecurity


