x, y = map(int, input().split())
count = 0
for n in range(x, y + 1):
    s = 0
    for c in str(n):
        s += int(c)
    if s % 5 == 0:
        count = count + 1
print(count)