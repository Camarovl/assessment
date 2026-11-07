try:
    while True:
        line = input().strip()
        if line == "":
            continue
        n = int(line)
        for i in range(1, n + 2):
            print(" " * (2 * (n + 1 - i)) + "*" * i)
        for i in range(n, 0, -1):
            print(" " * (2 * (n + 1 - i)) + "*" * i)
except EOFError:
    pass