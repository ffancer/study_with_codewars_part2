def solve(a, b):
    alice_cnt, bob_cnt = 0, 0

    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        else:
            if a[i] > b[i]:
                alice_cnt += 1
            else:
                bob_cnt += 1

    return f'{alice_cnt}, {bob_cnt}: Alice made "Kurt" proud!' if alice_cnt > bob_cnt else \
        f'{alice_cnt}, {bob_cnt}: Bob made "Jeff" proud!' if bob_cnt > alice_cnt else \
            f'{alice_cnt}, {bob_cnt}: that looks like a "draw"! Rock on!'


print(solve([47, 7, 2], [47, 7, 2]), '0, 0: that looks like a "draw"! Rock on!')
print(solve([47, 49, 22], [26, 47, 12]), '3, 0: Alice made "Kurt" proud!')
print(solve([25, 50, 22], [34, 49, 50]), '1, 2: Bob made "Jeff" proud!')
