"""
Сегодня 40 дней
"""

def projectPartners(n):
    return (n * (n - 1)) // 2


print(projectPartners(2), 1)
print(projectPartners(3), 3)
print(projectPartners(4), 6)
print(projectPartners(5), 10)
