## Short: "Cleartext Passwords in Code"

---

## Text

Stop putting passwords directly in your code.

I know. You know. And now strings knows too.

Here is a C file with a hardcoded password. We compile it. We run strings on the binary.
There it is. Sitting in your compiled binary like it owns the place.

"But I use an environment variable!" - Cool. Still there if you handle it wrong.

If it ends up in your binary, strings will find it.
Your grandma will find it.
And she will not be happy.

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
