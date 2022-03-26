def solution(n):
    dct = {4: 7,
           7: 4}
    return dct.get(n)

print(solution(7), 4)
print(solution(4), 7)
