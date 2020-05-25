class Solution():
    def threeSum(self, nums):
        res = []
        n = len(nums)
        nums = sorted(nums)
        for i in range(n-2):
            if i>0 and nums[i-1] == nums[i]:
                continue
            low = i+1
            high = n-1 
            while low<high:
                if nums[i] + nums[low] + nums[high] == 0:
                    res.append([nums[i], nums[low], nums[high]])
                    while low+1<n and nums[low] == nums[low+1]:
                        low += 1
                    while high-1>=0 and nums[high] == nums[high-1]:
                        high -= 1
                    high -= 1
                    low += 1
                elif nums[i] + nums[low] + nums[high]<0:
                    low += 1
                else:
                    high -= 1
        return res 

nums_1 = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums_1))
nums_2 = [0, -1, 2, -3, 1]
print(Solution().threeSum(nums_2))