# -*- config: utf-8 -*-

def product(*nums):
    if len(nums)==0:
        return 0
    ans = 1
    for num in nums:
        ans *= num
    return ans

print("Case 1: ", product())
print("Case 2: ", product(3))
print("Case 3: ", product(5, 6))
print("Case 4: ", product(5, 6, 7))
print("Case 5: ", product(5, 6, 7, 9))
