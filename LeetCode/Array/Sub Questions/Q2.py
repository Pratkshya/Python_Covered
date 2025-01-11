# 2. Find All Pairs
# Return all pairs that sum up to the target.
def twoSum(nums, target):
    isSeen = {}
    pairs = []
    for num in nums:
        diff = target - num
        if diff in isSeen:
            pairs.append([diff, num])
        isSeen[num] = "seen"
    return pairs    

nums = [3, 5, 1, 7, 5]
target = 8
print(twoSum(nums,target))