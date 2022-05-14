def part(arr):
    lst = ['Partridge', 'PearTree', 'Chat', 'Dan', 'Toblerone', 'Lynn', 'AlphaPapa', 'Nomad']
    cnt = 0

    for i in arr:
        if i in lst:
            cnt += 1

    return "Mine's a Pint!" if cnt == 0 else f"Lynn, I've pierced my foot on a spike{cnt * '!'}"


print(part(["Grouse", "Partridge", "Pheasant"]), "Mine's a Pint!")
print(part(["Pheasant", "Goose", "Starling", "Robin"]), "Lynn, I've pierced my foot on a spike!!")
print(part(["Grouse", "Partridge", "Partridge", "Partridge", "Pheasant"]), "Mine's a Pint!!!")
print(part([]), "Lynn, I've pierced my foot on a spike!!")
print(part(
    ["Grouse", "Partridge", "Pheasant", "Goose", "Starling", "Robin", "Thrush", "Emu", "PearTree", "Chat", "Dan",
     "Square", "Toblerone", "Lynn", "AlphaPapa", "BMW", "Graham", "Tool", "Nomad", "Finger", "Hamster"]),
    "Mine's a Pint!!!!!!!!")
