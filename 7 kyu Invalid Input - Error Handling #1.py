def get_count(words):
    try:
        if not words or not isinstance(words, str):
            return {'vowels': 0, 'consonants': 0}
        ans = {'vowels': 0, 'consonants': 0}

        ans['vowels'] = sum(1 for i in words if i in 'aeiouAEIOU')
        ans['consonants'] = sum(1 for i in words if i not in 'aeiouAEIOU' and i.isalpha())
        return ans
    except:
        return {'vowels': 0, 'consonants': 0}



print(get_count('Test'), {"vowels": 1, "consonants": 3}, 'Should return 1 vowel and 3 consonants')
print(get_count('Here is some text'), {"vowels": 6, "consonants": 8}, 'Should return 6 vowel and 8 consonants')
print(get_count('To be a Codewarrior or not to be'), {"vowels": 12, "consonants": 13},
      'Should return 12 vowel and 13 consonants')
print(get_count('To Kata or not to Kata'), {"vowels": 8, "consonants": 9}, 'Should return 8 vowel and 9 consonants')
print(get_count('aeiou'), {"vowels": 5, "consonants": 0}, 'Should return 5 vowel and 0 consonants')
print(get_count('TEst'), {"vowels": 1, "consonants": 3}, 'Should return 1 vowel and 3 consonants')
print(get_count('HEre Is sOme text'), {"vowels": 6, "consonants": 8}, 'Should return 6 vowel and 8 consonants')
print(get_count(), {"vowels": 0, "consonants": 0}, 'Should return 0 vowel and 0 consonants')
print(get_count(['To Kata or not to Kata']), {"vowels": 0, "consonants": 0}, 'Should return 0 vowel and 0 consonants')
print(get_count(None), {"vowels": 0, "consonants": 0}, 'Should return 5 vowel and 0 consonants')
