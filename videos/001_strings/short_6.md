## Short: "Your Grandma Could Find This Password"

---

## Headline
Grandma Finds Your Password

## Text

No terminal. No tools. No skills.

Download a firmware binary. Open it in Notepad. Hit Ctrl+F. Type "password". Hit enter.

There it is. In plain text. Inside a compiled binary. On a device that ships to millions of homes.

That's not a hack. That's a search.

Your grandma could do this. And honestly? She should.

Now imagine what you find when you stop using Notepad — and start using the actual tool built for this.

That's what strings is for. Full video in the link.

---

## Display / CLI / Code

```
[Screen: Windows Desktop]
- Download firmware .bin file from vendor website
- Right-click → "Open with" → Notepad
- Notepad opens, screen fills with garbage characters and occasional readable text
- Hit Ctrl+F
- Type: password
- Notepad highlights a match: admin_password=supersecret123
```

```bash
# One terminal shot at the end as a teaser
strings firmware.bin | grep -i password
```

Show the same result appears instantly in the terminal. Cut.
