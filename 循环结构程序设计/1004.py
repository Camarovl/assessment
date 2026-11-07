t = int(input())
for a in range(t):
    n = int(input())
    for i in range(n):
        stars = n - 2 * abs(i - n // 2)
        print(('*' * stars).center(n))