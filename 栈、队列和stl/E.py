s = input().strip()
stack = []
for ch in s:
    if ch == 'b' and stack and stack[-1] == 'a':
        stack.pop()
    else:
        stack.append(ch)
if stack:
    print("Bad")
else:
    print("Good")