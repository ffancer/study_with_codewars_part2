def owned_cat_and_dog(cat_years, dog_years):
    cat_ans, dog_ans = 0, 0

    if cat_years < 15:
        cat_ans = 0
    cat_years -= 15
    if cat_years < 9:
        cat_ans = 1
    cat_ans = 2 + (cat_years - 9) // 4

    if dog_years < 15:
        dog_ans = 0
    dog_years -= 15
    if dog_years < 9:
        dog_ans = 1
    dog_ans = 2 + (dog_years - 9) // 5

    return [cat_ans, dog_ans]


print(owned_cat_and_dog(15, 15), [1, 1])
print(owned_cat_and_dog(24, 24), [2, 2])
print(owned_cat_and_dog(56, 64), [10, 10])
