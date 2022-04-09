def solve(a, b):
    alice_total, bob_total = 0, 0
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        else:
            alice_total += a[i]
            bob_total += b[i]
    return alice_total, bob_total
print(solve([47, 7, 2], [47, 7, 2]), '0, 0: that looks like a "draw"! Rock on!')
print(solve([47, 49, 22], [26, 47, 12]), '3, 0: Alice made "Kurt" proud!')
print(solve([25, 50, 22], [34, 49, 50]), '1, 2: Bob made "Jeff" proud!')
