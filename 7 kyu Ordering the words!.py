def order_word(s):
    return "Invalid String!" if not s else ''.join(sorted(s))


print(order_word("Hello, World!"), " !,HWdellloor")
print(order_word("bobby"), "bbboy")
print(order_word(""), "Invalid String!")
