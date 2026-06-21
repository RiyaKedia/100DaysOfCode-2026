#include <stdio.h>

#define STADIUMS 3
#define MAX_GOALS 3
#define PLAYERS 3

int main() {
    // Store goals for each stadium
    int goals[STADIUMS][MAX_GOALS] = {
        {15, 42, -1},   // Stadium 0
        {8, 67, -1},    // Stadium 1
        {23, 55, 80}    // Stadium 2
    };

    // Goal counts for players
    int playerGoals[PLAYERS] = {2, 3, 2};

    int totalGoals = 0;

    // Count total goals safely
    for (int i = 0; i < STADIUMS; i++) {
        for (int j = 0; j < MAX_GOALS; j++) {
            if (goals[i][j] != -1) {   // valid goal
                totalGoals++;
            }
        }
    }

    // Find top scorer
    int topScorer = 0;
    for (int i = 1; i < PLAYERS; i++) {
        if (playerGoals[i] > playerGoals[topScorer]) {
            topScorer = i;
        }
    }

    // Output results
    printf("Total Goals: %d\n", totalGoals);
    printf("Top Scorer: Player %d\n", topScorer + 1);

    // Display stadium goals
    for (int i = 0; i < STADIUMS; i++) {
        printf("Stadium %d goals: ", i);
        for (int j = 0; j < MAX_GOALS; j++) {
            if (goals[i][j] != -1) {
                printf("%d ", goals[i][j]);
            }
        }
        printf("\n");
    }

    return 0;
}