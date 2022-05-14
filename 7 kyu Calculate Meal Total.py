def calculate_total(subtotal, tax, tip):
    pass


tests = [
    [(5.00, 5, 10), 5.75],
    [(36.97, 7, 15), 45.10],
    [(0.00, 6, 18), 0.00],
    [(80.94, 0, 20), 97.13],
    [(54.96, 8, 0), 59.36],
]

for i in tests:
    print(calculate_total(i[0][0], i[0][1], i[0][2]))
