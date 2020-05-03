class Solution:
    def moveZeros(self, nums):
        last_of_zero = index = 0
        while index<len(nums):
            if nums[index]:
                temp = nums[index]
                nums[index] = nums[last_of_zero]
                nums[last_of_zero] = temp
                last_of_zero += 1
            index += 1
        return nums
nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
nums = [1, 2, 0, 2, 0, 1, 3, 4]
Solution().moveZeros(nums)
print(nums)