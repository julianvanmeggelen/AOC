
CARDS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
class Hand:
    def __init__(self, cards: str, bid:int):
        self.cards = cards
        self.bid = bid
        self.type = self.type_()

    def type_(self):
        counts = [self.cards.count(c) for c in CARDS]
        # check 5 of a kind
        if 5 in counts: return 6
        # check 4 of a kind
        if 4 in counts: return 5
        #check full house
        if 3 in counts and 2 in counts: return 4
        #check three of a kind
        if 3 in counts and not 2 in counts: return 3
        #check two pair
        if counts.count(2) == 2: return 2
        #check one pair
        if counts.count(2) == 1 and max(counts) == 2: return 1
        #check high card
        if max(counts) == 1: return 0
        
        raise ValueError("No type")
    
    def sort_key(self):
        return tuple([self.type] + [len(CARDS) - CARDS.index(c) for c in self.cards])


if __name__ == "__main__":
    lines = open('input.txt').readlines()
    hands = [Hand(_[0], int(_[1])) for _ in [_.split() for _ in lines] ]
    print(sum((i+1) * h.bid for i, h in enumerate(sorted(hands, key = lambda el: el.sort_key()))))
  
# 249748283


    


     

