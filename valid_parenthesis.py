def valid_parenthesis(s):
    stack=[]
    if len(s)%2!=0:
        return 0
    for i in s:
        if i in "{([":
            stack.append(i)
        elif i in "]})":
            if not i in stack and is_matching(stack[-1],i):
                return False
            stack.pop()
    return not stack
def is_matching(open_char, close_char):
    return (open_char == '(' and close_char == ')') or \
           (open_char == '{' and close_char == '}') or \
           (open_char == '[' and close_char == ']')
        
s=input()
print(valid_parenthesis(s))
    
