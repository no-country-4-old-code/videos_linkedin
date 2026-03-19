## Short: "Why does SSH have 49 email addresses?"

---

## Headline
SSH's 49 Fake Emails

## Text

Run an email regex on `/usr/bin/ssh`. You get 49 hits. In the most security-critical binary on your system. That looks bad.

But look at them. `chacha20-poly1305@openssh.com`. `keepalive@openssh.com`. `ping@openssh.com`. `no-more-sessions@openssh.com`. These aren't people. They're ciphers, MACs, and protocol messages.

The SSH RFC uses `name@domain` as a namespacing convention for vendor extensions. These strings show up in two distinct places.

During the handshake, client and server each send a comma-separated list of supported algorithm names — `chacha20-poly1305@openssh.com`, `aes256-gcm@openssh.com`, and so on. Both sides compare lists, pick the first match, and that's your cipher. After that, the string disappears — the agreed algorithm just runs silently. It's a capability advertisement, not an opcode.

The second place is inside extension messages. `no-more-sessions@openssh.com` travels as the named payload of an `SSH_MSG_GLOBAL_REQUEST` packet. The packet type is still a numeric opcode — 80 — but the payload contains the string as the request name. The server looks it up, recognizes the extension, and locks down the connection: no further session channels allowed. A security signal: "I'm done, don't let anyone sneak one in."

The `@domain` part exists so OpenSSH can invent new identifiers — `keepalive@openssh.com`, `ping@openssh.com` — without colliding with base RFC names or other vendors. It just happens to look exactly like an email address.

---

## Display / CLI / Code

```bash
# The alarm — 49 email addresses in your SSH binary
strings /usr/bin/ssh | grep -oE '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' | sort -u | wc -l
# 49

# The reveal — they're not people
strings /usr/bin/ssh | grep -oE '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' | sort -u | head -15
# aes128-gcm@openssh.com
# aes256-gcm@openssh.com
# chacha20-poly1305@openssh.com
# curve25519-sha256@libssh.org
# ecdsa-sha2-nistp256-cert-v01@openssh.com
# hmac-md5-96-etm@openssh.com
# ...

# The proof — SSH sends these over the wire
strings /usr/bin/ssh | grep "Requesting no-more-sessions"
# Requesting no-more-sessions@openssh.com
```
