def first_missing_positive(nums):
    for num in nums:
        while num>0 and num<=len(nums) and num != nums[num-1]:
            temp = nums[num-1]
            nums[num-1] = num 
            num = temp 
    for index in range(0, len(nums)):
        if index+1 != nums[index]:
            return index + 1
    return len(nums)+1

print(first_missing_positive([1,2,0]))
