# -*- coding: utf-8 -*-

def cal(*nums):
    ans_min=None
    ans_max=None
    for num in nums:
        if ans_min is None or ans_min>num:
            ans_min = num
        if ans_max is None or ans_max<num:
            ans_max = num
    return ans_min, ans_max

if cal()!=(None, None):
    print("Case 1: Failed!")
elif cal(7)!=(7,7):
    print("Case 2: Failed!")
elif cal(7,9)!=(7,9):
    print("Case 3: Failed!")
elif cal(5,3)!=(3,5):
    print("Case 4: Failed!")
elif cal(4,4,4)!=(4,4):
    print("Case 5: Failed!")
elif cal(5,3,1,2,4,6,0,2)!=(0,6):
    print("Case 6: Failed!")
else:
    print("Success!")
