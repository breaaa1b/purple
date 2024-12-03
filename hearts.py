import random

def play_trick(hand, lead):
    leader_card = random.choice(hand[lead])
    amount_played = [None] * 4
    amount_played[leader_card] = lead
    hand[lead].remove(leader_card)
    
    leader_suit = leader_card[-1]
    
    for i in range(1, 4):
        current = (lead + 1) % 4
        valid = [card for card in hand[current] if card[-1] == leader_suit]
        
        if valid:
            chosen = random.choice(valid)
        else:
            chosen = random.choice(hand[current])
        
        amount_played[current] = chosen
        hand[current].remove(chosen)
    
    
    total_leader = [(i, card) for i, card in enumerate(amount_played) if card[-1] == leader_suit]
    winner = max(total_leader, key = lambda x: card_value(x[1]))[0]
    
    return winner, amount_played


def card_value(card):
    suits = {'C': 0, 'D': 1, 'H': 2, 'S': 3}
    ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
                 '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return suits[card[-1]] * 100 + ranks[card[:-1]]