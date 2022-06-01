def sort_it(list_, n):
    return sorted(list_, key=lambda list_: list_[n - 1])


print(sort_it('bill, bell, ball, bull', 2), 'ball, bell, bill, bull', 'Sort by the second letter')
print(sort_it('cat, dog, eel, bee', 3), 'bee, dog, eel, cat', 'Sort by the third letter')
