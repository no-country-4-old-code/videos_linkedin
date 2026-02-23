# 025_Perf_Loop_Enrollment - Compiler Loop Unrolling

## Concept
Demonstrate how compilers unroll loops to improve performance and reduce branching overhead.

## Key Points
- Loop overhead: increment, compare, branch
- Loop unrolling processes multiple iterations per loop
- Reduces branch instructions and improves pipeline usage
- Compiler does this automatically with -O2/-O3
- Manual unrolling vs compiler unrolling
- Trade-off: code size vs performance

## Hook
"Why write the same code 8 times when you can loop? Performance, that's why."

## Practical Demo
- Simple loop summing array elements
- Compile with -O0: show assembly (loop with branches)
- Compile with -O3: show assembly (unrolled loop)
- Compare assembly instruction count
- Benchmark both versions
- Show `#pragma GCC unroll N` for manual control
- Demonstrate extreme unrolling impact on code size
- Use `perf stat` to show reduced branch instructions
