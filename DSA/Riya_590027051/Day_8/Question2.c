#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    
    // Input string
    printf("Enter a string: ");
    scanf("%s", str);

    int len = strlen(str);

    // Reverse and print
    for (int i = len - 1; i >= 0; i--) {
        printf("%c", str[i]);
    }

    return 0;
}