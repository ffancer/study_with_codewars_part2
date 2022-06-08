def good_vs_evil(good, evil):
    total_good, total_evil = sum(int(i) for i in good.split()), sum(int(i) for i in evil.split())

    return 'Battle Result: No victor on this battle field' if total_good == total_evil else \
        'Battle Result: Evil eradicates all trace of Good' if total_evil > total_good else \
            'Battle Result: Good triumphs over Evil'


print(good_vs_evil('1 1 1 1 1 1', '1 1 1 1 1 1 1'), 'Battle Result: Evil eradicates all trace of Good')
print(good_vs_evil('0 0 0 0 0 10', '0 1 1 1 1 0 0'), 'Battle Result: Good triumphs over Evil')
print(good_vs_evil('1 0 0 0 0 0', '1 0 0 0 0 0 0'), 'Battle Result: No victor on this battle field')
