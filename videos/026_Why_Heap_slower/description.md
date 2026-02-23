# 026_Why_Heap_slower - Stack vs Heap Performance

## Concept
Explain why heap allocation is significantly slower than stack allocation.

## Key Points
- Stack: pointer bump (single instruction), automatic cleanup
- Heap: malloc/free complexity, fragmentation management, thread safety
- Stack has better cache locality (contiguous)
- Heap allocation involves syscalls or complex allocator algorithms
- Show real performance difference with benchmark
- When to use each: size, lifetime, and performance considerations

## Hook
"Stack allocation: 1 nanosecond. Heap allocation: 100 nanoseconds. Why?"

## Practical Demo
- Benchmark stack vs heap allocation
- Simple program allocating many small objects
- Version 1: local variables (stack)
- Version 2: malloc/free (heap)
- Measure time difference (100x+ faster for stack)
- Use `perf` to show syscall overhead
- Show assembly: stack is just RSP adjustment
- Show assembly: heap calls malloc (complex)
- Demonstrate cache effects with larger allocations
