# Time complexity O(n) and Space complexity O(1)
def sortNums(nums):
    lo = mid = 0
    hi = len(nums)-1
    while mid<=hi:
        if nums[mid] == 1:
            nums[lo], nums[mid] = nums[mid], nums[lo]
            lo += 1
            mid += 1
        elif nums[mid] == 2:
            mid += 1
        else:
            nums[hi], nums[mid] = nums[mid], nums[hi]
            hi -= 1
    return nums

print(sortNums([3, 3, 2, 1, 3, 2, 1]))