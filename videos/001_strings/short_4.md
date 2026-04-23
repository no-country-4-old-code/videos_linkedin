## Short: "Why does SSH have 49 email addresses?"

---

## Headline
SSH's 49 Fake Emails

## Text

Extract all strings in ssh, filter for email-addresses using grep and a regular expression, then filter the unique ones and count the lines.
You get 49 hits.
49 hardcoded email-addresses in one of the most security-critical binries on your system.

Reason enough to take a deeper look... *pause*
..which thankfully calms the situation. These aren't people. They're how SSH negotiates encryption.

During the handshake, client and server exchange lists of supported algorithm names. Both sides compare, pick the first match, and that's your cipher. The string disappears after that — the agreed algorithm just runs silently.

`no-more-sessions@openssh.com` is a different thing. It travels inside an extension message, and when the server sees it, it locks the connection: no further session channels allowed. A security signal: "I'm done, don't let anyone sneak one in."

So the `@domain` here is just namespacing — so OpenSSH can invent identifiers without colliding with base RFC names. It just happens to look exactly like an email address.

---

## Display / CLI / Code

https://datatracker.ietf.org/doc/html/rfc4251

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

---

## Youtube title
1. Why Does Your SSH Binary Contain 49 Email Addresses?
2. 49 Fake Email Addresses Hidden Inside SSH — Here's What They Actually Are
3. Reading SSH With `strings`: The "Email Addresses" That Are Really Cipher Names
4. What Are All Those `@openssh.com` Strings Actually Doing in Your SSH Binary?

## Youtube Description
Running `strings` on `/usr/bin/ssh` and filtering for email-shaped patterns returns 49 hits — but none of them are real addresses. They're RFC-defined algorithm identifiers: cipher names, key exchange methods, and extension signals like `no-more-sessions@openssh.com` that lock a connection once a session is established. A great example of how seemingly alarming binary content has a completely mundane explanation once you know the protocol.

Commands shown:
- `strings /usr/bin/ssh | grep -oE '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' | sort -u | wc -l`
- `strings /usr/bin/ssh | grep -oE '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' | sort -u | head -15`
- `strings /usr/bin/ssh | grep "Requesting no-more-sessions"`

#infosec #ssh #strings #binaryanalysis #cybersecurity

## LinkedIn Description
When a binary audit surfaces unexpected strings, cross-reference the protocol spec before raising an alarm — the 49 "email addresses" in SSH are cipher negotiation identifiers defined in RFC 4251, not a sign of compromise. Build the habit: `strings` reveals the data, but context tells you whether it's a finding.

#blueteam #infosec #cybersecurity
