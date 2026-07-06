def card_game(cards):
    left = 0
    right = len(cards) - 1

    player1 = 0
    player2 = 0
    turn = 0

    while left <= right:
        if cards[left] >= cards[right]:
            pick = cards[left]
            left += 1
        else:
            pick = cards[right]
            right -= 1

        if turn % 2 == 0:
            player1 += pick
        else:
            player2 += pick

        turn += 1

    print(player1, player2)


# Input
n = int(input())
cards = list(map(int, input().split()))

# Output
card_game(cards)