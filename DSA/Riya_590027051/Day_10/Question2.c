#include <stdio.h>
#include <string.h>

int main() {
    char s[101];
    int i, j, count = 0;
    
    scanf("%s", s);

    for(i = 0; i < strlen(s); i++) {
        int unique = 1;

        for(j = 0; j < i; j++) {
            if(s[i] == s[j]) {
                unique = 0;
                break;
            }
        }

        if(unique) {
            count++;
        }
    }

    if(count % 2 == 0)
        printf("CHAT WITH HER!");
    else
        printf("IGNORE HIM!");

    return 0;
}