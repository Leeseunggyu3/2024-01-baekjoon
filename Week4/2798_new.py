N, M = map(int, input().split())
cards = list(map(int, input().split()))
max = 0

for first_card in range(N):
    for second_card in range(first_card + 1, N):
        for third_card in range(second_card + 1, N):
            if cards[first_card] + cards[second_card] + cards[third_card] <= M and cards[first_card] + cards[second_card] + cards[third_card] >= max:
                max = cards[first_card] + cards[second_card] + cards[third_card]

print(max)
