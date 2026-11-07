c=input()
n=ord(c)-ord('A')+1
for i in range(1,n+1):
    print(' '*(n - i),end='')
    for j in range(i):
        print(chr(ord('A')+j),end='')
    for j in range(i-2,-1,-1):
        print(chr(ord('A')+j), end='')
    print()