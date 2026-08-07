def football_championship_winner(goals):
    # Dictionary to store goals scored by each team
    score = {}

    for team in goals:
        score[team] = score.get(team, 0) + 1

    # Find the team with the highest number of goals
    winner = max(score, key=score.get)

    return winner


# Input
goals = input("Enter the teams that scored: ").split()

# Find and print the winner
print("Winner:", football_championship_winner(goals))