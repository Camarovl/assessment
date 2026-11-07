t = input().strip()
p = t + t[-2::-1]
n = int(p)
def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 2
    return True
if is_prime(n):
    print("prime")
else:
    print("noprime")