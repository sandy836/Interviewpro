class Solution: 
    def getRange(self, arr, target):
        low = 0
        high = len(arr)-1
        while low<=high:
            mid = (high+low)//2
            if arr[mid] == target:
                return self.getFirstLastIndex(mid, arr, target)
            if target<arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1]
    
    def getFirstLastIndex(self, index, arr, target):
        first_index = last_index = index
        for i in range(index, len(arr)):
            if arr[i] == target:
                last_index = i
            else:
                break
        
        for i in range(index, -1, -1):
            if arr[i] == target:
                first_index = i
            else:
                break
        
        return [first_index, last_index]
        
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 8
print(Solution().getRange(arr, x))