def find_relative_ranks(score):
    # Sort scores in descending order
    sorted_scores = sorted(score, reverse=True)

    # Assign ranks
    rank_map = {}
    for i, s in enumerate(sorted_scores):
        if i == 0:
            rank_map[s] = "Gold Medal"
        elif i == 1:
            rank_map[s] = "Silver Medal"
        elif i == 2:
            rank_map[s] = "Bronze Medal"
        else:
            rank_map[s] = str(i + 1)

    # Build result in original order
    return [rank_map[s] for s in score]


# Input
score = list(map(int, input("Enter scores: ").split()))

# Output
result = find_relative_ranks(score)
print(result)