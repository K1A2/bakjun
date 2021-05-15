n, m = map(int, input().split())
cards = list(map(int, input().split()))
count = len(cards)
larger = 0
for i in range(count):
    for j in range(i + 1, count):
        for k in range(j + 1, count):
            answer = cards[i] + cards[j] + cards[k]
            if answer <= m and answer > larger:
                larger = answer
print(larger)