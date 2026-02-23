# 023_CPU_Cache - Memory Locality and Performance

## Concept
Explain CPU cache and demonstrate why memory access patterns dramatically affect performance.

## Key Points
- L1, L2, L3 cache hierarchy
- Cache lines (typically 64 bytes)
- Spatial locality: accessing nearby memory
- Contiguous memory access is cached efficiently
- Fragmented access causes cache misses
- Show cache info: `lscpu` or `/sys/devices/system/cpu/cpu0/cache/`

## Hook
"Same data, same operations, but one is 100x faster. The secret? Cache locality."

## Practical Demo
- Program accessing 2D array row-wise vs column-wise
- Measure performance difference
- Use `perf stat -e cache-references,cache-misses` to show cache behavior
- Demonstrate struct layout affecting cache performance
- Show difference between array-of-structs vs struct-of-arrays
- Visualize memory layout and cache lines
- Demonstrate cache-friendly vs cache-hostile code
