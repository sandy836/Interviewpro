def findPythagoreanTriplets(nums):
    _hash = set()
    length = len(nums)
    for i in range(0, length):
        square_i = nums[i]*nums[i]
        for j in range(i+1,length):
            _hash.add(square_i + nums[j]*nums[j])
    for i in range(0, length):
        if nums[i]*nums[i] in _hash:
            return True
    return False
    
print(findPythagoreanTriplets([10, 4, 6, 12, 5]))

print(findPythagoreanTriplets([3, 5, 12, 5, 13]))