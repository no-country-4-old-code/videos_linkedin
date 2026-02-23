# 024_CPU_Nr_of_arguments - Function Arguments and Performance

## Concept
Explain calling conventions and why the number of function arguments affects performance.

## Key Points
- x86-64 calling convention: first 6 args in registers (RDI, RSI, RDX, RCX, R8, R9)
- Additional arguments go on the stack (slower)
- Registers are fast, stack access is slower
- Show assembly code with different argument counts
- Measure performance difference
- Readability vs performance trade-off

## Hook
"More function parameters don't just hurt readability. They literally slow down your code."

## Practical Demo
- Function with 4 arguments (all registers)
- Function with 8 arguments (2 on stack)
- Compare assembly code with `objdump -d`
- Show register usage vs stack operations
- Benchmark both versions
- Use `perf stat` to measure instructions and cycles
- Demonstrate compiler optimizations with inlining
