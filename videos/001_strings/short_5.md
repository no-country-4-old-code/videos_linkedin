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
