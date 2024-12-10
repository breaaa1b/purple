import random

SUITS = ["C", "D", "H", "S"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
DECK =  [rank + suit for suit in SUITS for rank in RANKS ]

class Player:
    """ A valid Player
    
    Attributes:
        name (str): the player's name
        hand (list): the cards belongs to the player for current play
        collected_tricks (list): the cards received when winning the trick
    """
    def __init__(self, name):
        """ Primary author: Sharon Zhang
        Initialize a Player object.
        
        Args:
            name (str): a string that stored as player's name
        
        Side effects:
            Define name, hand, and collected_tricks attributes
        """
        self.name = name
        self.hand = []
        self.collected_tricks = []
    
    def receive_cards(self, cards):
        """ Primary authoer: Breanna Bernardino 
        Recive the cards deal by the computer randomly
        
        Args:
            cards (list): a list of cards deal by the computer from the start of 
            every round.
        
        Side effects:
            Modify hand attributes, store cards for each player
        """
        self.hand.extend(cards)
    
    def play_card(self, lead_suit=None, is_first_trick=False):
        """ Primary author: Sharon Zhang
        This method let player play their card for game
        
        Args:
            lead_suit (str): optional if the first trick for current player;
            consist of the leading suit for current trick
            is_first_trick (bool): optional if not the frist trick; if not the 
            first trick, the player need to follow different rules; if first 
            trick, the leading suit can be decided by the player
        
        Raises:
            NotImplementedError(): HumanPlayer and ComputerPlayer override this
            method due to different way of playing games
        """
        raise NotImplementedError()
    
    def collect_trick(self, cards):
        """ Primary author: Sharon Zhang
        Allow player collect the cards if winning the trick
        Args:
            cards (list): if ended up with the highest number of the suit, the
            player will be able to collect all four cards played for current 
            trick for calculating scores
        
        Side effects:
            Modify collected_tricks attributes, store cards for scores for each
            player
        """
        self.collected_tricks.extend(cards)
    
    def calculate_score(self):
        """ Primary author: Sharon Zhang
            Techniques: conditional expression
        Calculating scores based on the cards player collected through
        every trick
        
        Returns:
            int: the score calculated based on the rules; One heart card will 
            worth 1pt, One Queen of Spades worth 13pt. 
        """
        score = 0
        
        hearts = [card for card in self.collected_tricks if "H" in card]
        queen_of_spades = "QS" in self.collected_tricks
        score += len(hearts)
        if queen_of_spades:
            score += 13
        return score
    
    def reset(self):
        """ Primary author: Sharon Zhang
        Reset the game for another round
        
        Side effects:
            Modify hand and collected_tricks for each player
        """
        self.hand.clear()
        self.collected_tricks.clear()
    
    def __str__(self):
        """ Primary author: Sharon Zhang
            Techniques: Magic methods other than __init__()
        Produce an informal string representation of current Player's name
        
        Returns:
            str: the string representation of current Player
        """
        return self.name

class HumanPlayer(Player):
    """ Represents a human player in Hearts game
        Sub-class of Player    
    """
    def play_card(self, lead_suit=None, is_first_trick=False):
        """ Primary author: Sharon Zhang
        Simulates player playing their card

        Args:
            lead_suit (str): the lead suit of the trick
            is_first_trick (bool): the first trick 
        
        Side effects:
            prints out varying messages guiding the player how to play   
            
        Returns:
            str: A string representation of player's card that they are 
            playing: card
        """
        print(f"\nNow is {self.name}'s turn!")
        print(f"Your hand: {self.hand}")
        while True:
            card = input("Enter the card to play: ").strip()
            if card in self.hand:
                if (lead_suit and 
                    not (lead_suit in card) and 
                    any(lead_suit in c for c in self.hand)):
                    print("You must follow the lead suit!")
                elif is_first_trick and ("H" in card or card == "QS"):
                    print("You cannot play Hearts or the Queen of Spades"
                          " on the first trick!")
                else:
                    self.hand.remove(card)
                    return card
            else:
                print("Invalid card. Try again!")

class ComputerPlayer(Player):
    """ Represemts a Computer Player in the Hearts Game
        Sub-class of Player
    """
    def play_card(self, lead_suit=None, is_first_trick=False):
        """ Primary authoer: Breanna Bernardino 
        Simulates NPC computer player playing their card
        
        Args:
            lead_suit (str): the lead suit of the trick
            is_first_trick (bool): the first trick
        
        Side effects:
            prints out name of Computer Player and what card they play
             
        Returns:
            str: A string representation of player's card that they are 
            playing: card 
        """
        valid_cards = [card for card in self.hand 
                       if lead_suit 
                       if None or lead_suit in card]
        if not valid_cards:
            valid_cards = self.hand
        
        if is_first_trick:
            valid_cards = [card for card in valid_cards 
                           if "H" not in card and card != "QS"]
        
        card = valid_cards[0]
        self.hand.remove(card)
        print(f"{self.name} plays {card}")
        
        return card

class Game:
    """Represents game of hearts
    
    Attributes:
        player_num (int): amount of players playing
        deck(list): represents the deck of cards
        players (list) : contains the players of the game
        scores (dict) : consist of players with their scores
        max_score (int) : the maximum score of the current game that player
        could customize by their self
        current_leader (Player) : represents the current leader of the game
    """
    def __init__(self, player_num, max_score=100):
        """ Initializes new hearts game
        Author: Breanna Bernardino
        
        Args:
            player_num (int): amount of players playing the game
            max_score (int): the max score of the game 
            
        Side effects:
            Sets up initial game state
            Define basic attributes for game to start
        """
        self.player_num = player_num
        self.deck = DECK[:]
        self.players = []
        self.scores = {}
        self.max_score = max_score
        self.current_leader = None
    
    def setup_players(self):
        """ Setting up players according to the number of players
        Author: Breanna Bernardino
        
        Side effects:
            Modify players and scores attributes to setup for new game
            Ask input for name
        """
        self.players.append(HumanPlayer(input("Please enter your name: ")))
        for i in range(1, self.player_num):
            self.players.append(ComputerPlayer(f"Computer #{i}"))
        self.scores = {player.name: 0 for player in self.players}
    
    def card_deck(self):
        """ Setting up the card deck for the game
        Author: Breanna Bernardino
        
        Side effects:
            Modify deck attributes to fit the number of players
            Print out adject deck complete information for players
        """
        if self.player_num == 3:
            self.deck.remove("2D")
        elif self.player_num == 5:
            self.deck.remove("2C")
        print(f"Adjusted deck for {self.player_num} player. {len(self.deck)}"
              " cards in total right now. ")
    
    def shuffle_and_deal(self):
        """ Begin the game by randomly shuffle the card deck and deal the cards
        for each player based on the number of player
        Author: Sharon Zhang
        
        Side effects:
            Print out shuffled complete messgae for players.
        """
        random.shuffle(self.deck)
        print(f"Cards have been shuffled.")
        
        for i, card in enumerate(self.deck):
            self.players[i % self.player_num].receive_cards([card])
    
    def play_trick(self):
        """Simulates a trick being played
        Author: Breanna Bernardino
        Techniques: f-string, key function with lambda

            Returns:
            winner(Player): winner (player object) of the current trick
            
            Side effects:
            prints out that the winner won the current trick
            modifies self.current_leader to be the winner 
        """
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
        
        winner.collect_trick([card for player, card in trick])
        print(f"{winner.name} wins this trick!\n")
        
        self.current_leader = winner
        return winner
        
    def calculate_scores(self):
        """Calculates scores for players in current game
        Author: Sharon Zhang
        
        Side effects:
            prints name of player that shot the moon if round_score is 26
            modifies self.score according to player.name 
        """
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
        """ Perform each round of game
        Author: Sharon Zhang
        
        Side effects:
            Print out current leader for player
            Print out scores after each round
        """
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
        """Begins and ends the hearts game
        Author: Sharon Zhang
        
        Side Effects:
            prints out that the game is over, who the winner is, 
            and what their score is once the while loop is finished executing
        """
        self.setup_players()
        self.card_deck()
        
        while True:
            for score in self.scores.values():
                if score >= self.max_score:
                    print("\nGame Over!")
                    winner = min(self.scores, key=self.scores.get)
                    print(f"The winner is {winner} with a score of "
                          f"{self.scores[winner]}!")
                    break
            else:
                self.play_round()
                continue
            break # break out if game is over

if __name__ == "__main__":
    print("Welcome to Hearts Card Game!")
    
    max_score = input("Please enter the max score if you want: ")    
    while True:
        try:
            player_num = int(input("Enter the number of players (3-5): "))
            if player_num in [3, 4, 5]:
                break
            print("Invalid choice. Please enter a number 3-5")
        except ValueError:
            print("Invalid input. Please enter a number.")   
    
    if int(max_score):
        print(f"Max score will be: {max_score}")
        game = Game(player_num, max_score=int(max_score))
        game.play_game()
    else:
        game = Game(player_num)
        game.play_game()
        
    