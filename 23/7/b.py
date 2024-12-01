
CARDS = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
class Hand:
    def __init__(self, cards: str, bid:int):
        self.cards = cards
        self.bid = bid
        self.type = self.type_()

    def _make_combs(self, cards, i):
        res = []
        for card in cards:
            for c in CARDS:
                res.append(card[:i] + c + card[i+1:])
        return res


    def _get_all_combs(self, cards):
        joker_inds = [i for i, v in enumerate(self.cards) if v == 'J']
        res = [self.cards]
        for i in joker_inds:
            res = self._make_combs(res, i)
        return res

    def type_(self):
        all_combs = self._get_all_combs(self.cards)
        scores = []
        for comb in all_combs:
            counts = [comb.count(c) for c in CARDS]

            # check 5 of a kind
            if 5 in counts: return 6
            # check 4 of a kind
            if 4 in counts: 
                scores.append(5)
            #check full house
            if 3 in counts and 2 in counts: 
                scores.append(4)
            #check three of a kind
            if 3 in counts and not 2 in counts: 
                scores.append( 3)
            #check two pair
            if counts.count(2) == 2: 
                scores.append(2)
            #check one pair
            if counts.count(2) == 1 and max(counts) == 2: 
                scores.append(1)
            #check high card
            if max(counts) == 1: 
                scores.append(0)
        return max(scores)
        
        raise ValueError("No type")
    
    def sort_key(self):
        return tuple([self.type] + [len(CARDS) - CARDS.index(c) for c in self.cards])



if __name__ == "__main__":
    lines = open('input.txt').readlines()
    hands = [Hand(_[0], int(_[1])) for _ in [_.split() for _ in lines] ]
    print(sum((i+1) * h.bid for i, h in enumerate(sorted(hands, key = lambda el: el.sort_key()))))
  
# 249748283


    


     

