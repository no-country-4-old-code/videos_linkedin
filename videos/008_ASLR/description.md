# 008_ASLR - Address Space Layout Randomization

## Concept
Explain how ASLR protects against memory exploitation by randomizing memory addresses.

## Key Points
- Show memory addresses of stack, heap, and libraries without ASLR (predictable)
- Demonstrate the same program with ASLR enabled (different addresses each run)
- Explain why this matters for security: attackers can't hardcode memory addresses
- Use `/proc/self/maps` to visualize memory layout
- Compare addresses across multiple program executions
- Show how to check ASLR status: `cat /proc/sys/kernel/randomize_va_space`

## Hook
"Run your program twice. Why are the memory addresses completely different? That's ASLR protecting you."

## Practical Demo
- Simple C program printing stack and heap addresses
- Run without ASLR: `setarch $(uname -m) -R ./program`
- Run with ASLR: `./program`
- Show `/proc/self/maps` differences
- Demonstrate that exploits relying on fixed addresses fail with ASLR
