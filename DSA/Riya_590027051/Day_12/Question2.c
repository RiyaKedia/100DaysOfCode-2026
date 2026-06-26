#include <stdio.h>
#include <string.h>

int main() {
    int widths[26];
    char s[1001];

    // Input widths array
    for (int i = 0; i < 26; i++) {
        scanf("%d", &widths[i]);
    }

    // Input string
    scanf("%s", s);

    int lines = 1;
    int currentWidth = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        int charWidth = widths[s[i] - 'a'];

        if (currentWidth + charWidth > 100) {
            lines++;
            currentWidth = charWidth;
        } else {
            currentWidth += charWidth;
        }
    }

    // Output result
    printf("%d %d\n", lines, currentWidth);

    return 0;
}