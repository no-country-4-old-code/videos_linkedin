## Short: "Compilation Is Not Encryption"

---

## Text

A lot of developers think: I compiled the code, the source is gone, the secret is safe.
It isn't.

Here is a C file with a hardcoded password. We compile it. We run strings on the binary.
There it is. Sitting in your compiled binary like it owns the place.

Your compiler does not encrypt strings. It does not hide them. It just translates them into machine code — and strings reads right through that.

Compilation is a build step, not a security boundary.
If the value lives in your source, it lives in your binary.
And if it lives in your binary, strings can read it.

---

## Display / CLI / Code

```c
// code.c
#include <stdio.h>
int main() {
    char *password = "Sup3rS3cr3t!";  // hardcoded - bad!
    printf("Auth: %s\n", password);
    return 0;
}
```

```bash
gcc code.c -o code
strings code | grep -i "sup3r\|secret\|pass"
```

Show: password appears in binary output immediately.

```bash
# "clever" env variable approach - still leaks if stored in char*
strings code_env | grep -i "secret"
```
