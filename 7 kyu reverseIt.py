def reverse_it(data):
    if type(data) in [int, str, float]:
        return type(data)(str(data)[::-1])
    return data


print(reverse_it('Hello'), "olleH", 'Not quite')
print(reverse_it(314159), 951413, 'Not quite')
print(reverse_it("314159"), "951413", 'Not quite')
