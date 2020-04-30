def witnesses(heights):
    stack = []
    for height in heights:
        while stack and stack[-1]<=height:
            stack.pop()
        stack.append(height)
    return len(stack)

print(witnesses([3, 6, 3, 4, 9]))
print(witnesses([10, 6, 5, 4, 3]))
print(witnesses([4, 6, 3, 4, 1]))
print(witnesses([4, 4, 4, 4, 4]))
