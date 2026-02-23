# 015_Shared_lib_on_flight - Load Your Own .so During Runtime

## Concept
Dynamically load shared libraries at runtime using dlopen/dlsym instead of static linking.

## Key Points
- dlopen() loads shared libraries on demand
- dlsym() retrieves function pointers
- Plugin architectures use this technique
- Reduce startup time and memory by lazy loading
- Hot-reload functionality for development
- Error handling with dlerror()

## Hook
"Your program doesn't need to know about plugins at compile time. Load code on the fly."

## Practical Demo
- Main program with plugin interface
- Create multiple .so plugins implementing same interface
- Use dlopen() to load plugin by name at runtime
- Call plugin functions through dlsym()
- Switch plugins without restarting program
- Show ldd before and after loading
- Demonstrate hot-reload during debugging
