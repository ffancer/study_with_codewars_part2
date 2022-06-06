# 7 kyu
# Which section did you scroll to?


def get_section_id(scroll, sizes):
    total = 0
    for i in range(len(sizes)):
        if total - 1 < len(sizes):
            return i - 1
        else:
            total += sizes[i]
        if total - 1 >= scroll:
            return i
    # return -1


print(get_section_id(299, [300, 200, 400, 600, 100]), 0)
print(get_section_id(300, [300, 200, 400, 600, 100]), 1)
print(get_section_id(1600, [300, 200, 400, 600, 100]), -1)
