## Short: "Obfuscating Just the Password Is Not Security"

---

## Headline
Obfuscation Is Not Enough

## Text

You obfuscated the password. Good start. Not enough.

The username is sitting in cleartext — that's your signpost.
Search for it. Get the offset. Peek with xxd.

Username, right there. And next to it? Gibberish. That's your obfuscated password.
You can't read it — but you know exactly where it lives and roughly how long it is.

Field names like `password=` or `auth_key=` sitting next to the blob confirm what it is.
And simple obfuscation — base64, XOR, ROT13 — is trivially reversible once you know the location.

Obfuscation is not encryption. You gave the attacker a map.
Hash passwords with a real KDF. Don't obfuscate them.

---

## Display / CLI / Code

```bash
# Find username and its memory offset
strings -t x firmware-update-v4.2 | grep -Ff common_user_names.txt
# Output: 0x814d admin

# Peek at memory around that offset
xxd -s 0x814d -l 0x40 firmware-update-v4.2
# Output: username in cleartext, followed by unreadable bytes (the obfuscated password)

# One-liner to show how trivially the obfuscation falls apart
echo "cGFzc3dvcmQxMjM=" | base64 -d
# Output: password123
```

Show: username found at offset → xxd dump with username readable + garbled bytes next to it → base64 decode revealing the secret in one shot.
