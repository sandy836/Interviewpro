class Solution:
    def minSubArrayLen(self, nums, s):
        sum_dict = dict()
        cum_sum = sum_dict[0] = 0
        min_length = float('inf')
        for i in range(0, len(nums)):
            cum_sum += nums[i]
            if cum_sum-s in sum_dict:
                if (i-sum_dict[cum_sum-s]+1) < min_length:
                    min_length = i-sum_dict[cum_sum-s]+1
            sum_dict[cum_sum] = i+1
        return min_length 

print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 9))
print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 15))