#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_WORDS 1000
#define MAX_LEN 1001

char* mostCommonWord(char* paragraph, char** banned, int bannedSize) {
    char words[MAX_WORDS][MAX_LEN];
    int count[MAX_WORDS] = {0};
    int wordCount = 0;

    char temp[MAX_LEN];
    int idx = 0;

    // Convert paragraph into words
    for (int i = 0;; i++) {
        char ch = paragraph[i];

        if (isalpha(ch)) {
            temp[idx++] = tolower(ch);
        } else {
            if (idx > 0) {
                temp[idx] = '\0';

                // Check if banned
                int bannedFlag = 0;
                for (int j = 0; j < bannedSize; j++) {
                    if (strcmp(temp, banned[j]) == 0) {
                        bannedFlag = 1;
                        break;
                    }
                }

                // If not banned, count frequency
                if (!bannedFlag) {
                    int found = -1;
                    for (int j = 0; j < wordCount; j++) {
                        if (strcmp(words[j], temp) == 0) {
                            found = j;
                            break;
                        }
                    }

                    if (found != -1) {
                        count[found]++;
                    } else {
                        strcpy(words[wordCount], temp);
                        count[wordCount] = 1;
                        wordCount++;
                    }
                }
                idx = 0;
            }
        }

        if (ch == '\0') break;
    }

    // Find most frequent word
    int maxFreq = 0;
    int maxIndex = 0;

    for (int i = 0; i < wordCount; i++) {
        if (count[i] > maxFreq) {
            maxFreq = count[i];
            maxIndex = i;
        }
    }

    // Return result
    char* result = (char*)malloc(strlen(words[maxIndex]) + 1);
    strcpy(result, words[maxIndex]);

    return result;
}