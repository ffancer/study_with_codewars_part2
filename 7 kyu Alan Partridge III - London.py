def alan(arr):
    lst = ['Rejection', 'Disappointment', 'Backstabbing Central', 'Shattered Dreams Parkway']
    cnt = 0

    for i in arr:
        if i in lst:
            cnt += 1

    return 'Smell my cheese you mother!' if cnt == 4 else 'No, seriously, run. You will miss it. '


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
