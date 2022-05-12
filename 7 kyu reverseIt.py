def reverse_it(data):
    return str(data)[::-1] if type(data) in [str, int] else data


print(reverse_it('Hello'), "olleH", 'Not quite')
print(reverse_it(314159), 951413, 'Not quite')
print(reverse_it("314159"), "951413", 'Not quite')
