# 007_rust_bloated - Why Rust Binaries are Bloated

## Concept
Explore why Rust binaries are significantly larger than equivalent C/C++ programs.

## Key Points
- Compare binary sizes: simple "Hello World" in Rust vs C
- Show that Rust statically links the standard library by default
- Demonstrate the impact of including panic handling, formatting, and other runtime features
- Use tools like `size`, `nm`, and `bloaty` to analyze binary composition
- Show optimization techniques: `strip`, `--release`, `opt-level`, `lto`, `panic=abort`
- Demonstrate size reduction from ~4MB to <500KB with proper flags

## Hook
"Why is a simple Rust 'Hello World' 100x larger than in C? Let me show you what's hiding in your binary."

## Practical Demo
- Compile same program in Rust and C
- Compare sizes with `ls -lh`
- Analyze sections with `size` and `nm`
- Apply optimization flags step by step
- Show dramatic size reduction
