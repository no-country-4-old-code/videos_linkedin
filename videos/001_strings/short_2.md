## Short: "Finding Passwords by Username"

---

## Text

What if the password is obfuscated... but the username isn't?

Sometimes you don't search for the password directly.
You search for the username instead.

With `-t x` you get the exact memory location of the string.
Then you peek around that spot with xxd.

And there it is. Username. Password. Right next to each other in memory.
Like a sticky note taped to the front door.

Classic.

---

## Display / CLI / Code

```bash
# Find usernames and their memory offsets
strings -t x firmware-update-v4.2 | grep -Ff common_user_names.txt

# Peek at the memory around that offset
xxd -s 0x814d -l 0x40 firmware-update-v4.2
```

Show output: username found at offset, then xxd dump revealing password sitting right next to it in memory.
