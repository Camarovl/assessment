from itertools import permutations
out = []
for p in permutations("12345678"):
    out.append(" ".join(p))
print("\n".join(out))