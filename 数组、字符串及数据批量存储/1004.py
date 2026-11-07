L, M = map(int, input().split())
tree = []
for i in range(L + 1):
    tree.append(True)
for i in range(M):
    l, r = map(int, input().split())
    for j in range(l, r + 1):
        tree[j] = False
cnt = 0
for i in range(L + 1):
    if tree[i]:
        cnt += 1
print(cnt)