def find_e(s):
    if not s:
        return s

    cnt = s.lower().count('e')

    return str(cnt) if cnt != 0 else "There is no \"e\"."


print(find_e('actual'), "There is no \"e\".")
print(find_e('English'), '1')
print(find_e('English exercise'), '4')
print(find_e(''), '')
print(find_e(None), None)
