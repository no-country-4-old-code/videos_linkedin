## Short: "What Is strings?"

---

## Headline
Read Binaries Like Books

## Text

Shipped with binutils comes one of the most useful CLI tools to extract strings from binaries: `strings`.

Use `-t x` to show the offset of each string in hex — great for reverse engineering. Use `-n` to set a minimum length and cut through the noise.

For more options, check the man page. Pretty useful tool. Been there for ages, but still absolutely worth it.

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
