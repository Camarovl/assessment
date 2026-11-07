L, R = map(int, input().split())
count = 0
for i in range(L, R + 1):
    count += str(i).count('2')
print(count)