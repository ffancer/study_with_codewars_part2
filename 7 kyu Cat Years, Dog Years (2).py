def owned_cat_and_dog(cat_years, dog_years):
    cat_ans, dog_ans = 0, 0

    if cat_years == 15:
        cat_ans += 1
    elif cat_years == 24:
        cat_ans += 2
    else:
        cat_ans = (cat_years - 24) // 4 + 2

    if dog_years == 15:
        dog_ans += 1
    elif dog_years == 24:
        dog_ans += 2
    else:
        dog_ans = (dog_years - 24) // 5 + 2

    return cat_ans, dog_ans


print(owned_cat_and_dog(15, 15), [1, 1])
print(owned_cat_and_dog(24, 24), [2, 2])
print(owned_cat_and_dog(56, 64), [10, 10])
