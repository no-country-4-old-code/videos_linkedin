#include <stdio.h>
void some_function(int, int, int);

int global_var = 1;

void main() {
    int local_var = 2;
    static int static_var = 3;
    some_function(global_var, local_var, static_var);
}

void some_function(int a, int b, int c) {
    printf("%d, %d and %d\n", a, b, c);
}
