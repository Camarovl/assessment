n = int(input())
nums = input().split()
for i in range(n - 1):
    for j in range(n - 1 - i):
        a, b = nums[j], nums[j + 1]
        if a + b < b + a:
            nums[j], nums[j + 1] = b, a
ans = ""
for x in nums:
    ans += x
print(ans)