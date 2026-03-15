## Short: "What Is strings?"

---

## Text

One command. Every secret a binary tries to hide.

`strings` extracts human-readable text from binary files. It ships with binutils. It's been around since the early Unix days — we're talking 1970s and 80s.

And it still works. On everything.

Firmware dumps. Malware samples. Compiled executables. IoT device images. `strings` doesn't care. It finds the text the developer left behind and hands it to you.

Hidden URLs. Hardcoded credentials. Error messages. Version strings. All of it.

Something this old and this simple is still the first tool security analysts reach for. That should tell you something.

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
