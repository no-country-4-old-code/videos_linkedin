# 030_RFID_Scanning_with_Cameleon_Ultra - Cloning RFID Cards with the Chameleon Ultra

## Concept
Demonstrate how the Chameleon Ultra can read, clone, and emulate RFID / NFC access cards — showing why physical access control based solely on card UID is insecure.

## Key Points
- What the Chameleon Ultra is: a research-grade RFID multi-tool
- Read a Mifare Classic / RFID card and dump its UID
- Clone the card onto the Chameleon Ultra
- Emulate the cloned card to open a reader
- Brief note on defenses: encrypted sector auth, rolling codes, secondary factors

## Hook
"This office card gets you through the door. Let me clone it in three seconds."

## Practical Demo
- Use the Chameleon Ultra CLI to scan a card
- Show the raw UID and sector data in the terminal
- Write the clone and switch to emulation mode
- Present the Chameleon to a reader — door opens
