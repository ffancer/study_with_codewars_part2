class HTMLGen:
    def a(self, text):
        return f'<a>{text}</a>'

    def b(self, text):
        return f'<b>{text}</b>'

    def p(self, text):
        return f'<p>{text}</p>'

    def body(self, text):
        return f'<body>{text}</body>'

    def div(self, text):
        return f'<div>{text}</div>'

    def span(self, text):
        return f'<span>{text}</span>'

    def title(self, text):
        return f'<title>{text}</title>'

    def comment(self, text):
        return f'<!--{text}-->'


htmlGen = HTMLGen()
print(htmlGen.a('test'), '<a>test</a>')
print(htmlGen.comment('test'), '<!--test-->')
