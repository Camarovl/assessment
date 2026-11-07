import sys
mdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for line in sys.stdin:
    if not line.strip():
        continue
    y, m, x = map(int, line.split())
    d = mdays[m - 1]
    if m == 2 and ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
        d = 29
    count = 0
    for day in range(1, d + 1):
        count += ("%04d%02d%02d" % (y, m, day)).count(str(x))
    print(count)