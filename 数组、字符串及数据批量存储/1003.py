n, k, m = map(int, input().split())
people = []
for i in range(n):
    people.append(i)
idx = k 
while len(people) > 1:
    idx = (idx + m - 1) % len(people)
    people.pop(idx)
    idx = idx % len(people)
print(people[0])