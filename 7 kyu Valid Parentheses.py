def valid_parentheses(paren_str):

    if paren_str == '' or paren_str[0] == '(' and paren_str.count('(') == paren_str.count(')'):
        return True

    return False



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