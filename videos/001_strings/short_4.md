## Short: "Easter Eggs Hidden in Your Linux Tools"

---

## Text

Your Linux tools have secrets the developers left behind.

TODOs. Debug messages. Internal URLs. Sarcastic comments buried in production binaries.

Because developers are human. And humans leave notes.
They just forget those notes ship to millions of machines.

One strings command. That's all it takes to read their mind.

Developers are humans too.
They just hide their personality in the binary.

---

## Display / CLI / Code

```bash
# SSH has opinions
strings /usr/bin/ssh | grep -i "todo\|hack\|fixme\|http"

# curl too
strings /usr/bin/curl | grep -i "todo\|debug\|fixme\|internal"

# git is very talkative
strings /usr/bin/git | grep -i "TODO\|FIXME\|hack\|joke"
```

Show interesting/funny output lines: internal hostnames, TODO notes, debug strings, hardcoded URLs, etc.
