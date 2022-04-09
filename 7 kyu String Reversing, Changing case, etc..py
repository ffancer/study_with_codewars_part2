def reverse_and_mirror(s1, s2):
    return s2.swapcase()[::-1] + '@@@' + s1[::-1].swapcase() + s1.swapcase()


print(reverse_and_mirror('FizZ', 'buZZ'), 'zzUB@@@zZIffIZz')
print(reverse_and_mirror('String Reversing', 'Changing Case'),
      'ESAc GNIGNAHc@@@GNISREVEr GNIRTssTRING rEVERSING')
