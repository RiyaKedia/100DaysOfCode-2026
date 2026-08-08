import heapq


def maximum_playlist_pleasure(length, beauty, k):
    # Combine length and beauty
    songs = list(zip(length, beauty))

    # Sort by beauty in descending order
    songs.sort(key=lambda x: x[1], reverse=True)

    min_heap = []
    total_length = 0
    max_pleasure = 0

    for l, b in songs:
        # Add current song
        heapq.heappush(min_heap, l)
        total_length += l

        # Keep at most k songs
        if len(min_heap) > k:
            removed = heapq.heappop(min_heap)
            total_length -= removed

        # Current beauty is the minimum beauty
        pleasure = total_length * b

        max_pleasure = max(max_pleasure, pleasure)

    return max_pleasure


# Input
length = list(map(int, input("Enter song lengths: ").split()))
beauty = list(map(int, input("Enter beauty values: ").split()))
k = int(input("Enter k: "))

# Calculate maximum pleasure
answer = maximum_playlist_pleasure(length, beauty, k)

print("Maximum Playlist Pleasure:", answer)