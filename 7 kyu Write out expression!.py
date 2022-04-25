def expression_out(exp):
    dct = {'0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight',
           '9': 'Nine', '10': 'Ten', "+": "Plus", "-": "Minus", "*": "Times", "/": "Divided By", "**": "To The Power Of",
           "=": "Equals", "!=": "Does Not Equal"}
    lst = []

    for i in exp.split():
        if i in dct.keys():
            lst.append(dct[i])
    return ' '.join(lst)


print(expression_out('1 + 3'), 'One Plus Three')
print(expression_out('2 - 10'), 'Two Minus Ten')
print(expression_out('6 ** 9'), 'Six To The Power Of Nine')
print(expression_out('5 = 5'), 'Five Equals Five')
print(expression_out('7 * 4'), 'Seven Times Four')
print(expression_out('2 / 2'), 'Two Divided By Two')
print(expression_out('8 != 5'), 'Eight Does Not Equal Five')
