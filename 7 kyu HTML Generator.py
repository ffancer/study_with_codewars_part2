class HTMLGen:
    def a(self, text):
        return f'<a>{text}</a>'


htmlGen = HTMLGen()
print(htmlGen.a('test'), '<a>test</a>')
print(htmlGen.comment('test'), '<!--test-->')
