class Solution:
    def isValid(self, s):
        stack = []
        open_bracket = ['(', '{', '[']
        close_bracket = [')', '}', ']']
        for char in s:
            if char in open_bracket:
                stack.append(char)
            elif len(stack)>0 and stack[-1] == open_bracket[close_bracket.index(char)]:
                stack.pop()
            else:
                return False
        if len(stack)>0:
            return False
        return True

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
