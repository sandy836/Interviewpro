import heapq
#Heap based approch
def findKthLargestHeapApproch(nums, k):
    ans = nums[:k]
    heapq.heapify(ans)
    for num in nums[k:]:
        if ans[0]<num:
            heapq.heappushpop(ans, num)
    return ans[0]
#Quick Select Approch in-place
def partition(arr, left, right):
    pivot = arr[left]
    leftMark = left+1
    rightMark = right
    while True:
        while leftMark<right and arr[leftMark]<pivot:
            leftMark += 1
        while rightMark>left and arr[rightMark]>pivot:
            rightMark -= 1
        if leftMark>=rightMark:
            break
        else:
            temp = arr[leftMark]
            arr[leftMark] = arr[rightMark]
            arr[rightMark] = temp
    temp = arr[left]
    arr[left] = arr[leftMark-1]
    arr[leftMark-1] = temp
    return leftMark-1

def findKthLargest(arr, left, right, k):
    if left == right:
        return arr[left]
    split = partition(arr, left, right)
    length = split-left+1
    if length == k:
        return arr[split]
    if k<length:
        return findKthLargest(arr, left, split-1, k)
    else:
        return findKthLargest(arr, split+1, right, k-length)
arr = [3, 5, 2, 4, 6, 8]
length, k = len(arr), 2
print(findKthLargestHeapApproch(arr, k))
print(findKthLargest(arr, 0, length-1, length-k+1))