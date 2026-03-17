## Short: "Obfuscating Just the Password Is Not Security"

---

## Text

You obfuscated the password. Doesn't matter.

If the username is sitting in cleartext, it's a signpost pointing straight at the password.
Search for the username. Get the memory offset.
Peek around that spot with xxd.

And there it is. Username. Password. Right next to each other in memory.

The false sense of security: you hid the password but left the username, the config key, the surrounding context completely exposed.
Any one of those is a map to the secret you thought you buried.

Partial obfuscation is not a security boundary.

---

## Display / CLI / Code

```bash
# Find usernames and their memory offsets
strings -t x firmware-update-v4.2 | grep -Ff common_user_names.txt

# Peek at the memory around that offset
xxd -s 0x814d -l 0x40 firmware-update-v4.2
```

Show output: username found at offset, then xxd dump revealing password sitting right next to it in memory.
