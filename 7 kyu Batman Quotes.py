class BatmanQuotes(object):

    @staticmethod
    def get_quote(quotes, hero):
        return f"{('Batman', 'Joker', 'Robin')['BJR'.index(hero[0])]}: {quotes[int(min(hero))]}"


quotes = ["WHERE IS SHE?!", "Holy haberdashery, Batman!", "Let's put a smile on that faaaceee!"]
print(BatmanQuotes.get_quote(quotes, "Rob1n"), "Robin: Holy haberdashery, Batman!")