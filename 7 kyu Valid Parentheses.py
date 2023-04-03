def valid_parentheses(paren_str):
    lst = []
    for i in paren_str:
        if i == '(':
            lst.append(i)
            continue
        lst.pop()
    return lst

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