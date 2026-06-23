#include <stdio.h>
#include <string.h>

int main() {
    char str[100], result[100];
    int i, j = 0;

    // Input string
    fgets(str, sizeof(str), stdin);

    // Remove spaces
    for (i = 0; str[i] != '\0'; i++) {
        if (str[i] != ' ' && str[i] != '\n') {
            result[j] = str[i];
            j++;
        }
    }

    result[j] = '\0';

    // Output modified string
    printf("%s", result);

    return 0;
}