## Short: "What Is strings?"

---

## Headline
Read Binaries Like Books

## Text

Shipped with binutils is `strings` — a tool that extracts strings from binaries.

Use `-t x` to show the offset of each string in hex.
Very useful to find out where to look with the hex editor.

Use `-n` to set a minimum length and minimize the noise.

For more options, check the man page. Pretty useful tool.

It's been there for ages, but still absolutely worth it.
In the following videos we will have some fun with it.

---

## Display / CLI / Code

```bash
# What version are we running?
strings --version

# Show strings longer than 10 chars from a real binary
strings -n 10 /usr/bin/ls | head -20

# Show offset (hex) of each string — useful for reverse engineering
strings -t x /usr/bin/ls | head -20

# Quick peek at the man page
man strings | head -30
```

Show output: version info, recognizable strings from `ls` binary (paths, error messages, format strings), then hex offsets to hint at deeper use cases.

---

## Youtube title
1. The One Linux Tool That Reads Binaries Like Plain Text
2. `strings`: Extract Human-Readable Data From Any Binary in Seconds
3. How Attackers Start Analyzing a Binary — With a Tool Already on Your System
4. What Is `strings` and Why Every Security Engineer Should Know It?

## Youtube Description
`strings` ships with binutils and extracts printable character sequences from any binary. Use `-n` to filter out noise by setting a minimum length, and `-t x` to get the hex offset of each hit — useful for jumping straight to the right location in a hex editor.

Commands shown:
- `strings --version`
- `strings -n 10 /usr/bin/ls | head -20`
- `strings -t x /usr/bin/ls | head -20`
- `man strings | head -30`

#infosec #strings #binaryanalysis #linux #cybersecurity

## LinkedIn Description
Before your binaries leave the build pipeline, run `strings -n 8` on them — it takes seconds and will surface hardcoded credentials, internal paths, or debug artefacts that have no business shipping to a customer.

#devsecops #appsec #cybersecurity
