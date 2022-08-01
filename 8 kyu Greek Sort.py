greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu',
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')


def greek_comparator(lhs, rhs):
    return


print(greek_comparator('alpha', 'beta'), "result should be negative")
print(greek_comparator('psi', 'psi'), 0)
print(greek_comparator('upsilon', 'rho'), "result should be positive")
