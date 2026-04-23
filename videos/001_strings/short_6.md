## Short: "Your Grandma Could Find This Password"

---

## Headline
Grandma Finds Your Password

## Text

Everytime I see someone using cleartext password - direct or indirect - it gives me bad vibes.
Its like.. "Hey, lets deploy the password directly to the customer"
Even your grandma could open this file here with the way-to-boring windows text editor to read out the password.
Something YOUR grandma of course would NEVER do.
Because she is a damn professional. She would use a better tool for that - like strings. 

---

## Display / CLI / Code

Same as in script.md .
Basically I just use the first section.
Maybe personal video for shorts would also not be needed.
Screenshot of my for first image is enough.

---

## Youtube title
1. Even Your Grandma Could Extract This Cleartext Password
2. Cleartext Password in a Binary: A Grandma With `strings` Finds It Instantly
3. Why Shipping Cleartext Passwords in Binaries Is Still a Thing in 2025
4. How Easy Is It to Find a Hardcoded Password? This Easy.

## Youtube Description
Hardcoded cleartext passwords in firmware or application binaries are trivially extractable — no reverse engineering knowledge required. The `strings` tool, which ships with every Linux system, is all it takes to read them out. This short illustrates why any secret embedded in a binary is effectively public.

Commands shown:
- `strings <binary>`
- `strings -t x <binary>`

#infosec #hardcodedcredentials #strings #firmware #cybersecurity

## LinkedIn Description
If a password lives in a binary, treat it as compromised — `strings` on the artifact exposes it with zero effort. Scan every build artifact for credentials before shipping, and enforce that secrets come from environment variables or a secrets manager at runtime, never from the compiled binary.

#devsecops #appsec #cybersecurity
