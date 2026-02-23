#include <stdio.h>
#include <string.h>

void check_password(const char *input) {
    const char *correct = "supersecret";
    if (strcmp(input, correct) == 0) {
        printf("Access granted!\n");
    } else {
        printf("Access denied.\n");
    }
}

int main() {
    char buffer[100];
    printf("Enter password: ");
    fgets(buffer, sizeof(buffer), stdin);

    // Remove newline
    buffer[strcspn(buffer, "\n")] = 0;

    check_password(buffer);

    return 0;
}
