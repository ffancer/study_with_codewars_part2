def remove_chars(s):
    return ''.join(i for i in s if i.isalpha() or i == ' ')


print(remove_chars("test for error!"), "test for error", 'remove_chars("test for error!") did not return correct value')
print(remove_chars(".tree1"), 'tree', 'remove_chars".tree1") did not return correct value')
