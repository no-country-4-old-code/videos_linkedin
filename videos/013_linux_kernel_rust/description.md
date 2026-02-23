# 013_linux_kernel_rust - How Rust is Used in Linux Kernel

## Concept
Show how Rust is being integrated into the Linux kernel for safer driver development.

## Key Points
- Rust in Linux kernel since version 6.1
- Focus on driver development (network, storage, etc.)
- Memory safety without garbage collection
- Show real example: Rust NVMe driver or network driver
- Compare LOC and safety of Rust vs C kernel module
- Compile and load a simple Rust kernel module

## Hook
"The Linux kernel, written in C for 30 years, is now getting Rust. Here's why that's a big deal."

## Practical Demo
- Show kernel version with Rust support
- Browse Rust kernel code in `rust/` directory
- Simple "Hello World" Rust kernel module
- Compile with kernel build system
- Load with `insmod` and check `dmesg`
- Compare with equivalent C kernel module
- Show safety features that prevent common C bugs
