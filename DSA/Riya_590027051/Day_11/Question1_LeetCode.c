#include <stdio.h>
#include <string.h>

int isIsomorphic(char s[], char t[]) {
    int mapST[256];
    int mapTS[256];

    // Initialize arrays with -1
    for (int i = 0; i < 256; i++) {
        mapST[i] = -1;
        mapTS[i] = -1;
    }

    int n = strlen(s);

    for (int i = 0; i < n; i++) {
        unsigned char c1 = s[i];
        unsigned char c2 = t[i];

        // Create mapping if not already present
        if (mapST[c1] == -1 && mapTS[c2] == -1) {
            mapST[c1] = c2;
            mapTS[c2] = c1;
        }
        // Check if mapping is invalid
        else if (mapST[c1] != c2 || mapTS[c2] != c1) {
            return 0;
        }
    }

    return 1;
}

int main() {
    char s[50001], t[50001];

    scanf("%s", s);
    scanf("%s", t);

    if (strlen(s) != strlen(t)) {
        printf("false\n");
        return 0;
    }

    if (isIsomorphic(s, t))
        printf("true\n");
    else
        printf("false\n");

    return 0;
}