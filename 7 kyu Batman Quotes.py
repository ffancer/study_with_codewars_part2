class BatmanQuotes(object):

    @staticmethod
    def get_quote(quotes, hero):
        return "Who" + ": " + "said what?"


quotes = ["WHERE IS SHE?!", "Holy haberdashery, Batman!", "Let's put a smile on that faaaceee!"]
print(BatmanQuotes.get_quote(quotes, "Rob1n"), "Robin: Holy haberdashery, Batman!")