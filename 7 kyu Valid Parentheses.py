def valid_parentheses(paren_str):
    cnt = 0

    for i in paren_str:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
            if cnt < 0:
                return False

    return cnt == 0


# all True
print(valid_parentheses("()"))
print(valid_parentheses("((()))"))
print(valid_parentheses("()()()"))
print(valid_parentheses("(()())()"))
print(valid_parentheses("()(())((()))(())()"))

# all False
print(valid_parentheses(")("))
print(valid_parentheses("()()("))
print(valid_parentheses("((())"))
print(valid_parentheses("())(()"))
print(valid_parentheses(")()"))
print(valid_parentheses(")"))

# "Should return True for empty strings"
print(valid_parentheses(""))