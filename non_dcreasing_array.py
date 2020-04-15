#Time complexity O(nlogn) and Space complexity O(1)
def check_1(nums):
    copy_1, copy_2 = nums[:], nums[:]
    for i in range(0, len(nums)-1):
        if nums[i]>nums[i+1]:
            copy_1[i] = nums[i+1]
            copy_2[i+1] = nums[i]
            break
    return copy_1 == sorted(copy_1) or copy_2 == sorted(copy_2)

#Time complexity O(n) and Space complexity O(1)
def check_2(nums):
    count = 0
    i = 1
    while i<len(nums):
        if nums[i-1]>nums[i] and count<=1:
            count += 1
            if i-2<0 or nums[i-2]<=nums[i]:
                nums[i-1] = nums[i]
            else:
                nums[i] = nums[i-1]
        i += 1
    return count<=1

print(check_1([13, 4, 7]))
print(check_2([5,1,3,2,5]))
