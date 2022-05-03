class HTMLGen:
    pass


htmlGen = HTMLGen()
print(htmlGen.a('test'), '<a>test</a>')
print(htmlGen.comment('test'), '<!--test-->')
