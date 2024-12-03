import random
def initialize(num):
    suits = ["C", "D", "H", "S"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [rank + suit for suit in suits for rank in ranks ]
    
    if num == 3:
        deck.remove("2D")
    elif num == 5:
        deck.remove("2C")
        
    random.shuffle(deck)
    hand = len(deck) // num
    hands = [deck[i * hand:(i + 1) * hand] for i in range (num)]
    return hands

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