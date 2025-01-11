# 2. Find All Pairs
# Return all pairs that sum up to the target.
def twoSum(nums, target):
    isSeen = {}
    pairs = set()
    for num in nums:
        diff = target - num
        if diff in isSeen:
            pairs.add((min(diff, num), max(diff, num)))
        isSeen[num] = "seen"
    return list(pairs)   

nums = [3, 5, 1, 7, 5]
target = 8
print(twoSum(nums,target))