#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char str[101];
    scanf("%s", str);

    int n = strlen(str);

    for (int i = 0; i < n; i++) {
        char ch = tolower(str[i]);

        // Skip vowels
        if (ch == 'a' || ch == 'e' || ch == 'i' || 
            ch == 'o' || ch == 'u' || ch == 'y') {
            continue;
        }

        // Print dot + consonant
        printf(".%c", ch);
    }

    return 0;
}