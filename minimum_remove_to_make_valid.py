def count_invalid_parenthesis(string):
    stack = []
    count = 0
    for char in string:
        if char == '(':
            stack.append(char)
        elif stack and stack[-1] == '(':
            stack.pop()
        else:
            count += 1 
    
    return count + len(stack)
print(count_invalid_parenthesis(")()())()"))