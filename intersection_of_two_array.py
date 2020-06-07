class Solution:
  def intersection(self, nums1, nums2):
    res = set()
    nums1.sort()
    nums2.sort()
    i = j = 0
    while i<len(nums1) and j<len(nums2):
        if nums1[i] == nums2[j]:
            res.add(nums1[i])
            i+=1
            j+=1
        elif nums1[i]>nums2[j]:
            j+=1
        else:
            i+=1
    return res 



print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))