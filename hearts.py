import random

SUITS = ["C", "D", "H", "S"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
DECK =  [rank + suit for suit in SUITS for rank in RANKS ]

class Game:
    def __init__(self, player_num):
        self.player_num = player_num
        self.deck = DECK[:]
        self.player = []
        self.trick = []
        self.scores = {}
    
    def card_deck(self):
        if self.player_num == 3:
            self.deck.remove("2D")
        elif self.player_num == 5:
            self.deck.remove("2C")
        print(f"Adjusted deck for {self.player_num} player. {len(self.deck)}"
              "cards in total right now. ")
    
    def shuffle_cards(self):
        random.shuffle(self.deck)
        print(f"Cards have been shuffled.")
        
def play_trick(hands, lead = None):
    players = len(hands)
    if players not in [3, 4, 5]:
        raise ValueError("This game only supports 3, 4, or 5 players only")
    
    if lead is None:
        starting = "2C" if num != 3 else "3C"
        for i, hand in enumerate(hands):
            if starting in hand:
                lead = i
                break
    
    
    if lead is None:
        raise ValueError("No starting card found in hand")
    
    lead_card = next(card for card in hands[lead] if card == ("2C" if players != 3 else "3C"))
    played_cards = [None] * players
    played_cards[lead] = lead_card
    hands[lead].remove(lead_card)
    lead_suit = lead_card[-1]