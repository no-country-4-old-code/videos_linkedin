# 010_data_rss_bss - Different Places to Store Data

## Concept
Explain the different memory segments where data is stored: .data, .rodata, .bss, heap, and stack.

## Key Points
- .data segment: initialized global/static variables
- .rodata: read-only data (const strings, etc.)
- .bss: uninitialized global/static variables (zero-initialized)
- heap: dynamic memory (malloc/new)
- stack: local variables and function calls
- Show segment sizes with `size` command
- Use `objdump -h` to inspect sections

## Hook
"Your program uses 5 different places to store data. Choose the wrong one, and your password ends up in the binary."

## Practical Demo
- C program with different types of variables
- Use `size` to show segment sizes
- Use `nm` and `objdump` to show where each variable lives
- Demonstrate that .bss doesn't bloat file size
- Show how const data ends up in .rodata (read-only)
- Extract strings from each segment with `strings -a -t x`
