import random

SUITS = ["C", "D", "H", "S"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
DECK =  [rank + suit for suit in SUITS for rank in RANKS ]

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.collected_tricks = []
    
    def receive_cards(self, cards):
        self.hand.extend(cards)
    
    def play_card(self, lead_suit=None, is_first_trick=False):
        raise NotImplementedError()
    
    def collect_trick(self, cards):
        self.collected_tricks.extend(cards)
    
    def calculate_score(self):
        score = 0
        hearts = [card for card in self.collected_tricks if "H" in card]
        queen_of_spades = "QS" in self.collected_tricks
        score += len(hearts)
        if queen_of_spades:
            score += 13
        return score
    
    def reset(self):
        self.hand.clear()
        self.collected_tricks.clear()
    
    def __str__(self):
        return self.name

class HumanPlayer(Player):
    """Represents a human player in Hearts game

        Side effects:
        prints out varying messages guiding the player how to play
    """
    def play_card(self, lead_suit=None, is_first_trick=False):
        """Simulates player playing their card

            Args:
            lead_suit: None
            the lead suit of the trick
            is_first_trick: bool
            the first trick 
            
            
            Returns:
            str
            A string representation of player's card that they are playing: card
        """
        print(f"\nNow is {self.name}'s turn!")
        print(f"Your hand: {self.hand}")
        while True:
            card = input("Enter the card to play: ").strip()
            if card in self.hand:
                if lead_suit and not (lead_suit in card) and any(lead_suit in c for c in self.hand):
                    print("You must follow the lead suit!")
                elif is_first_trick and ("H" in card or card == "QS"):
                    print("You cannot play Hearts or the Queen of Spades on the first trick")
                else:
                    self.hand.remove(card)
                    return card
            else:
                print("Invalid card. Try again!")

class ComputerPlayer(Player):
    def play_card(self, lead_suit=None, is_first_trick=False):
        valid_cards = [card for card in self.hand if lead_suit if None or lead_suit in card]
        if not valid_cards:
            valid_cards = self.hand
        
        if is_first_trick:
            valid_cards = [card for card in valid_cards if "H" not in card and card != "QS"]
        
        card = valid_cards[0]
        self.hand.remove(card)
        print(f"{self.name} plays {card}")
        
        return card

class Game:
    def __init__(self, player_num, max_score=100):
        self.player_num = player_num
        self.deck = DECK[:]
        self.players = []
        self.trick = []
        self.scores = {}
        self.max_score = max_score
        self.current_leader = None
    
    def setup_players(self):
        self.players.append(HumanPlayer("You"))
        for i in range(1, self.player_num):
            self.players.append(ComputerPlayer(f"Computer #{i}"))
        self.scores = {player.name: 0 for player in self.players}
    
    def card_deck(self):
        if self.player_num == 3:
            self.deck.remove("2D")
        elif self.player_num == 5:
            self.deck.remove("2C")
        print(f"Adjusted deck for {self.player_num} player. {len(self.deck)}"
              " cards in total right now. ")
    
    def shuffle_and_deal(self):
        random.shuffle(self.deck)
        print(f"Cards have been shuffled.")
        num_cards = len(self.deck)
        for i, card in enumerate(self.deck):
            self.players[i % self.player_num].receive_cards([card])
    
    def play_trick(self):
        trick = []
        lead_suit = None
        
        start_index = self.players.index(self.current_leader)
        
        for i in range(len(self.players)):
            player = self.players[(start_index + i) % len(self.players)]
            card = player.play_card()
            
            if not trick:
                lead_suit = card[-1]
            
            trick.append((player, card))
        
        winning_card = max(
            [card for player, card in trick if card[-1] == lead_suit],
            key=lambda c:RANKS.index(c[:-1])
        )
        winner = next(player for player, card in trick if card == winning_card)
        
        winner.collect_trick([card for card in trick])
        print(f"{winner.name} wins this trick!\n")
        
        self.current_leader = winner
        return winner
        # if lead_suit is None:
        #     starting = "2C" if self.player_num != 3 else "3C"
        #     for i, hand in enumerate(self.hand):
        #         if starting in hand:
        #             lead = i
        #             break
        #     if lead is None:
        #         raise ValueError("No starting card found in hand")
    
    # lead_card = next(card for card in hands[lead] if card == ("2C" if players != 3 else "3C"))
    # played_cards = [None] * players
    # played_cards[lead] = lead_card
    # hands[lead].remove(lead_card)
    # lead_suit = lead_card[-1]
    def calculate_scores(self):
        for player in self.players:
            round_score = player.calculate_score()
            if round_score == 26:
                print(f"{player.name} shot the moon!")
                for opponent in self.players:
                    if opponent != player:
                        self.scores[opponent.name] += 26
            else:
                self.scores[player.name] += round_score
                
    def play_round(self):
        self.shuffle_and_deal()
        if not self.current_leader:
            lead_card = "3C" if "2C" not in self.deck else "2C"
            for player in self.players:
                if lead_card in player.hand:
                    self.current_leader = player
                    break
        print(f"Starting Round with Leader: {self.current_leader}")
        
        for _ in range(len(self.deck) // self.player_num):
            self.play_trick()
            
        self.calculate_scores()
        print("\nScores after this round:")
        for name, score in self.scores.items():
            print(f"{name}: {score}")
        
        for player in self.players:
            player.reset()
    
    def play_game(self):
        self.setup_players()
        self.card_deck()
        
        while all(score < self.max_score for score in self.scores.values()):
            self.play_round()
        
        print("\nGame Over!")
        winner = min(self.scores, key=self.scores.get)
        print(f"The winner is {winner} with a score of {self.scores[winner]}!")

if __name__ == "__main__":
    print("Welcomd to Hearts Card Game!")
    
    while True:
        try:
            player_num = int(input("Enter the number of players (3-5): "))
            if player_num in [3, 4, 5]:
                break
            print("Invalid choice. Please enter a number 3-5")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    game = Game(player_num)
    game.play_game()