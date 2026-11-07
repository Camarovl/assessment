n, k = map(int, input().split())
morning = list(map(int, input().split()))
evening = list(map(int, input().split()))
gains = []
for i in range(n):
    gains.append(morning[i] - evening[i])
gains.sort(reverse=True)
best_gains = gains[:k]
total = sum(evening) + sum(best_gains)
print(total)