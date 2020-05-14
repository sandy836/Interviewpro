def trapped_water(heights):
    ans = leftMax = rightMax = 0
    left, right = 0, len(heights)-1
    while left<right:
        if heights[left]>leftMax:
            leftMax = heights[left]
        if heights[right]>rightMax:
            rightMax = heights[right]
        if(leftMax < rightMax):
            ans += leftMax-heights[left]
            left += 1
        else:
            ans += rightMax-heights[right]
            right -= 1
    return ans
 
print(trapped_water([0,1,0,2,1,0,1,3,2,1,2,1]))
