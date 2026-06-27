#include <stdio.h>
#include <string.h>

#define MAX 1000

// Function to count distinct subsequences
long long countDistinctSubseq(char str[]) {
    int n = strlen(str);
    long long dp[n + 1];
    int last[256];

    // Initialize last occurrence array
    for (int i = 0; i < 256; i++)
        last[i] = -1;

    dp[0] = 1; // Empty subsequence

    for (int i = 1; i <= n; i++) {
        dp[i] = 2 * dp[i - 1];

        if (last[(int)str[i - 1]] != -1) {
            dp[i] = dp[i] - dp[last[(int)str[i - 1]]];
        }

        last[(int)str[i - 1]] = i - 1;
    }

    return dp[n];
}

int main() {
    char s1[MAX], s2[MAX];

    scanf("%s %s", s1, s2);

    long long count1 = countDistinctSubseq(s1);
    long long count2 = countDistinctSubseq(s2);

    if (count1 >= count2)
        printf("%s\n", s1);
    else
        printf("%s\n", s2);

    return 0;
}