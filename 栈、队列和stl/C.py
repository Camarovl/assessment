n = int(input()) 
nums = list(map(int, input().split()))
nums.sort()
for i in range(n - 2):
    a, b, c = nums[i], nums[i + 1], nums[i + 2]
    if a + b > c:
        print(a, b, c)
print("No solution")