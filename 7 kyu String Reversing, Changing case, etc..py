def reverse_and_mirror(s1, s2):
    right_word = s1[::-1].swapcase() + s1.swapcase()
    return right_word


print(reverse_and_mirror('FizZ', 'buZZ'), 'zzUB@@@zZIffIZz')
print(reverse_and_mirror('String Reversing', 'Changing Case'),
      'ESAc GNIGNAHc@@@GNISREVEr GNIRTssTRING rEVERSING')
