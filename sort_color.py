class Solution:
  def sortColors(self, nums):
    mid = left = 0
    right = len(nums)-1
    while mid<=right:
        if nums[mid] == 0:
            nums[mid], nums[left] = nums[left], nums[mid]
            left += 1 
            mid += 1 
        elif nums[mid] == 1:
            mid += 1 
        else:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1
            
nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]