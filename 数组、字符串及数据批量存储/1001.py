T = int(input())
for t in range(T):
    n = int(input())
    a = []
    a += list(map(int, input().split()))
    s = 0
    s2 = 0
    mx = a[0]
    mn = a[0]
    for x in a:
        s += x
        s2 += x * x
        if x > mx:
            mx = x
        if x < mn:
            mn = x
    var = (n * s2 - s * s) / (n * n)     
    print(mx - mn, "%.3f" % var)