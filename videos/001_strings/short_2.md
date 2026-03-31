## Short: "Obfuscating Just the Password Is Not Security"

---

## Headline
Obfuscation Is Not Enough

## Text

You obfuscated the password. Nice try. Attackers might need a little bit longer to identify your password inside this whole binary garbage.

Unless you stored your obfuscated password directly beside your username.
Which is still in cleartext.
And not very creative.

So an attacker could simply search for it, get the offset and then peek around it with xxd.
Obfuscating passwords is not hashing.
It is reversible.

Do yourself a favor and hash your passwords with a real key derivation function.

---

## Display / CLI / Code

```bash
# Find username and its memory offset
strings -t x firmware-update-v4.2 | grep -Ff common_user_names.txt
# Output: 0x2020 admin

# Peek at memory around that offset
xxd -s 0x2020 -l 0x40 firmware-update-v4.2
# Output: username in cleartext, followed by unreadable bytes (the obfuscated password)

# One-liner to show how trivially the obfuscation falls apart
echo "cGFzc3dvcmQxMjM=" | base64 -d
# Output: password123
```

Show: username found at offset → xxd dump with username readable + garbled bytes next to it → base64 decode revealing the secret in one shot.
