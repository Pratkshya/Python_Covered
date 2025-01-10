
# 1. Find Two Numbers That Add Up to Target
# Return the numbers themselves instead of their indices.

def twoSum(nums, target):
    checkVal = {}
    for num in nums:
        requiedVal = target - num
        if requiedVal in checkVal:
            return [requiedVal, num]
        checkVal[num] = "seen"
    return []    

nums = [1,5,3,6]
target = 8
print(twoSum(nums, target))