# 7 kyu
# Which section did you scroll to?


def get_section_id(scroll, sizes):
    total = 0

    for i, size in enumerate(sizes):
        total += size
        if scroll >= total:
            continue
        else:
            return i
    return -1


print(get_section_id(299, [300, 200, 400, 600, 100]), 0)
print(get_section_id(300, [300, 200, 400, 600, 100]), 1)
print(get_section_id(1600, [300, 200, 400, 600, 100]), -1)
