import random
class Player:
    
    suits = ["C", "D", "H", "S"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    
    def initialize(num):
        deck = [rank + suit for suit in suits for rank in ranks]
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
   
    #determine starting player
        if lead is None:
            starting = "2C" if num != 3 else "3C"
            for i, hand in enumerate(hands):
                if starting in hand:
                    lead = i
                    break
    
    
        if lead is None:
            raise ValueError("No starting card found in hand")
    
    #lead player starts trick
        lead_card = next(card for card in hands[lead] if card == ("2C" if players != 3 else "3C"))
        played_cards = [None] * players
        played_cards[lead] = lead_card
        hands[lead].remove(lead_card)
        lead_suit = lead_card[-1]
        
        #other players play cards
        for i in range(1, players):
            current = (lead + i) % players
            valid_amount_cards = [card for card in hands[current] if card[-1] == lead_suit]
            
            if valid_amount_cards:
                chosen = max(valid_amount_cards, key=lambda card:{"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
            "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}[card[:-1]])
                
            else:
                non_hearts = [card for card in hands[current] if card[-1] != "H" and card != "QS"]
                chosen = random.choice(non_hearts if non_hearts else hands[current])
                
            played_cards[current] = chosen
            hands[current].remove(chosen)
        
        #determine winner
        lead_suits = [(i, card) for i, card in enumerate(played_cards) if card[-1] == lead_suit]
        winner = max(lead_suits, key=lambda x: {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
             "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}[x[1][:-1]])[0]
            
        return winner, played_cards