def fix(paragraph):
    lst = []

    for i in paragraph.split('. '):
        lst.append(i.capitalize())

    return '. '.join(lst)


print(fix(""), "")
print(fix("hi."), "Hi.")
print(
    fix("hello. my name is inigo montoya. you killed my father. prepare to die."),
    "Hello. My name is inigo montoya. You killed my father. Prepare to die.")
