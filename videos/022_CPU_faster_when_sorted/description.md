# 022_CPU_faster_when_sorted - Branch Prediction and Pipeline

## Concept
Demonstrate why processing sorted data can be dramatically faster than unsorted data due to branch prediction.

## Key Points
- CPU pipeline and speculative execution
- Branch predictor predicts if/else outcomes
- Sorted data = predictable branches = fast
- Random data = mispredictions = pipeline stalls
- Classic stackoverflow.com question example
- Measure performance with `perf stat` showing branch misses

## Hook
"Why is summing a sorted array 6x faster than an unsorted one? The answer will blow your mind."

## Practical Demo
- C/C++ program summing values above threshold
- Run with sorted array: measure time
- Run with unsorted array: measure time
- Show dramatic difference (5-6x)
- Use `perf stat -e branches,branch-misses` to show mispredictions
- Explain CPU pipeline visualization
- Show branchless optimization that eliminates the difference
