def alan(arr):
    lst = ['Rejection', 'Disappointment', 'Backstabbing Central', 'Shattered Dreams Parkway']

    for i in arr:
        if i in lst:
            idx = lst.index(i)
            del lst[idx]

    return 'Smell my cheese you mother!' if len(lst) == 0 else 'No, seriously, run. You will miss it.'


print(
    alan(["Norwich", "Rejection", "Disappointment", "Backstabbing Central", "Shattered Dreams Parkway", "London"]),
    "Smell my cheese you mother!")
print(alan(["London", "Norwich"]), "No, seriously, run. You will miss it.")
print(alan(["Norwich", "Tooting", "Bank", "Rejection", "Disappointment", "Backstabbing Central", "Exeter",
            "Shattered Dreams Parkway", "Belgium", "London"]), "Smell my cheese you mother!")
print(alan(["London", "Norwich"]), "No, seriously, run. You will miss it.")
print(
    alan(["London", "Shattered Dreams Parkway", "Backstabbing Central", "Disappointment", "Rejection", "Norwich"]),
    "Smell my cheese you mother!")
