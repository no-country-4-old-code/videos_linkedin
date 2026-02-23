# 012_mix_rust_c_c++ - Mixing Rust with C/C++ (ABI)

## Concept
Demonstrate how to call Rust from C/C++ and vice versa using FFI and ABI compatibility.

## Key Points
- ABI (Application Binary Interface) defines calling conventions
- C ABI is the universal standard for interoperability
- Rust functions need `extern "C"` and `#[no_mangle]` for C compatibility
- Use `cbindgen` to generate C headers from Rust
- Show linking process with both static and dynamic libraries
- Demonstrate passing data between Rust and C safely

## Hook
"Rust's safety, C's libraries. Why choose when you can have both?"

## Practical Demo
- Rust library with `extern "C"` functions
- Generate C header with cbindgen
- C program calling Rust functions
- Compile and link both together
- Show symbol mangling with/without `#[no_mangle]`
- Demonstrate safe string passing between languages
