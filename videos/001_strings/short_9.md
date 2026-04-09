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


