import collections

Card = collections.namedtuple("Card", ["rank", "sult"])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 12)] + list("JQKA")
    sults = "Spades dlamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, sult) for sult in self.sults for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def __str__(self):
        return self._cards
    

deck = FrenchDeck()

for card in reversed(deck):
    print(card)
