num_s = [
    1000, 900, 500, 400,
    100, 90, 50, 40,
    10, 9, 5, 4,
    1
]
let_s = [
    "M", "CM", "D", "CD",
    "C", "XC", "L", "XL",
    "X", "IX", "V", "IV",
    "I"
]


def solution(n):
    s = ''
    i = 0

    while n > 0:
        for _ in range(n // num_s[i]):
            s += let_s[i]
            n -= num_s[i]
        i += 1

    return s


print(solution(1), 'I', "solution(1),'I'")
print(solution(4), 'IV', "solution(4),'IV'")
print(solution(6), 'VI', "solution(6),'VI'")
print(solution(14), 'XIV', "solution(14),'XIV")
print(solution(21), 'XXI', "solution(21),'XXI'")
print(solution(89), 'LXXXIX', "solution(89),'LXXXIX'")
print(solution(91), 'XCI', "solution(91),'XCI'")
print(solution(984), 'CMLXXXIV', "solution(984),'CMLXXXIV'")
print(solution(1000), 'M', 'solution(1000), M')
print(solution(1889), 'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
print(solution(1989), 'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")
