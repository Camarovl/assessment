n = int(input())
a = list(map(int, input().split()))
c = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
nexts = []
for p in range(30):
    s = True
    for i in range(n):
        if c[(p + i) % 30] != a[i]:
            s = False
            break
    if s:
        nexts.append(c[(p + n) % 30])
last = a[n - 1]
up = True
down = True
for v in nexts:
    if v < last:
        up = False
    if v > last:
        down = False
if up and not down:
    print("UP")
elif down and not up:
    print("DOWN")
else:
    print("-1")