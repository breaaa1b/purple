# Final Project Proposal Version 2.0

- Group name: Purple
- Group Member: Breanna Bernardino, Sharon Zhang


- Concept Description:
Our program will allow users to play card game Hearts with other human players 
or computer players. Our program will allow 3-5 players and some rules will be slightly different depending on the number of players. Basically, the program 
will simulate the actual game. It will keep track of players' score at the end 
of each hand based on the hearts they have and the queen spade if they have. 
The game will be played to 100 points. When one player hits the agreed-upon 
score or higher, the game ends. And the player with the lowest score wins.


- Scoring function/method: Sharon
This function will calculate the score for each player at the end of each hand.
    - Hearts count as one point each and the queen counts 13 points;
    - Total of all scores for each hand must be a multiple of 26
    - If exactly get 26(13 hearts and one queen), score set to 0, but each of opponents score an additional 26
    - Is usually played to 100 points
Args:
    player (Player): current player (having a list attribute consist of all the 
    cards current play have)
Side Effects:
    - Modify current player’s score attribute
    - Print out score
Returns:
    Int: the score of current player


Play Trick function/method: Brea:
This function simulates a trick being played
-player deals one card or a trick is played
-player with the 2 of clubs starts trick or winner of the last trick after the first trick has already passed
-first card played = lead suit
-filter cards to only match lead suit (can’t play a heart or queen of spades on first trick)
-find highest card from the filtered cards
-return the highest card or the card that wins the trick

Args:
	-player_list: list of current players
Side effect:
	-prints out winning card of the trick
Returns: 
	Player: the winning card (highest card) 


