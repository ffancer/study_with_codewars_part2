def reverse_it(data):
    if type(data) is str:
        return data[::-1]
    elif type(data) is int:
        return int(str(data)[::-1])
    return data

print(reverse_it('Hello'), "olleH", 'Not quite')
print(reverse_it(314159), 951413, 'Not quite')
print(reverse_it("314159"), "951413", 'Not quite')
