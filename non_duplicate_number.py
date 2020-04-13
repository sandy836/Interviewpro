def singleNumber(nums):
    a = 0
    for num in nums:
        a ^= num
    return a
print(singleNumber([4, 3, 2, 4, 1, 3, 2]))