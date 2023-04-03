def valid_parentheses(paren_str):
    lst = []

    for i in paren_str:
        if i == '(':
            lst.append(i)
            continue
        if len(lst) == 0:
            return False
        lst.pop()

    return True if len(lst) == 0 else False


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