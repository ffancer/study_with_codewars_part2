def get_all_prime_factors(n):
    if not isinstance(n, int) or n <= 1:
        if n == 1:
            return [1]
        else:
            return []
    else:
        factors = []
        prime = 2
        while prime * prime <= n:
            while n % prime == 0:
                factors.append(prime)
                n //= prime
            prime += 1
        if n > 1:
            factors.append(n)
        return factors


def prime_factors(n):
    res = ""
    factors = get_all_prime_factors(n)

    for i in sorted(set(factors)):
        cnt = factors.count(i)
        if cnt == 1:
            res += f'({i})'
        else:
            res += f'({i}**{cnt})'
    return res


print(prime_factors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")
