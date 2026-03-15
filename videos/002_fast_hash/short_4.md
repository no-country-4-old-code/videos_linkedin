## Short: "The Easter Eggs Inside hashcat"

---

## Text

Even hacking tools have a sense of humor.

We used strings in the last video to dig secrets out of binaries. Let's turn it on hashcat itself.

Search for TODOs, debug comments, URLs left behind by developers.

And then scroll through the hash mode list. There are modes for ancient DOS password formats. Casino card games. Old Nokia phones. Obscure point-of-sale systems from 1998.

Someone sat down and implemented a cracker for every forgotten format in computing history.

Behind every security tool... there's a developer who thought this was funny at 3am.

---

## Display / CLI / Code

```bash
# Use strings on hashcat itself (callback to video 001!)
strings $(which hashcat) | grep -iE "todo|hack|lol|egg|debug|http"

# Hunt for funny or obscure hash mode names
hashcat --help | grep -iE "example|casino|nokia|atm|pos|legacy"

# Browse the full list — scroll slowly for effect
hashcat --help | grep "^[[:space:]]*[0-9]" | tail -80
```

Show output:
- `strings` revealing leftover URLs, debug tags, or dev comments in the binary
- Hash mode list showing oddly specific legacy formats (e.g. "descrypt, DES (Unix)", old gaming/ATM formats)
- Scroll slowly — let the absurdity of 300+ supported formats sink in
