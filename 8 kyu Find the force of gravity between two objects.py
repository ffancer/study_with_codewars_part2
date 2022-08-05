dct = {"kg": 1, "g": 1e-3, "mg": 1e-6, "μg": 1e-9, "lb": 0.453592,
       "m": 1, "cm": 1e-2, "mm": 1e-3, "μm": 1e-6, "ft": 0.3048,
       }


def solution(arr_val, arr_unit):
    m1, m2, r = (arr_val[i] * dct[arr_unit[i]] for i in range(3))
    return 6.67e-11 * m1 * m2 / r ** 2


print(solution([1000, 1000, 100], ["g", "kg", "m"]), 6.67e-12)
print(solution([1000, 1000, 100], ["kg", "kg", "m"]), 6.667e-9)
print(solution([1000, 1000, 100], ["kg", "kg", "cm"]), 0.0000667)
