# Final Project Proposal

- Group name: Purple


- Concept Description:
Our project will be a text adventure game where player could explore, engage in
battles, collect items, and defeat bosses. Throughout the whole storyline, 
player will be able to  encounter different types of enemies, acquire dropped 
items to help with their journey, gain experience from the battle to get new 
abilities. 


- Level function/method: Sharon
This method will track the leveling progress of the player, the new level will unlock new abilities.
- Args:
    Player: Player object that is current playing the game
    Player_xp: A attribute of player object; player’s current xp & level
- Returns:
    Return the current level and xp value (as a dict? Or set?)
- Side effects:
    Will update the level & xp attributes of current player
    When gain xp or level up, print the message to notify player


-Begin Battle function/method : Breanna
This method begins the battle between the player and whichever boss they encounter
-Args:
    player : Player object that is currently playing the game
    boss : boss object that player encounters
-Return: 
    nothing
-Side effects:
    -print out the name of the boss has appeared to the player 
	-if the player wins (if the boss’ health is less than or equal to zero), print out that the player has defeated boss name
	-if player loses (if player’s health is less than or equal to zero), print out player has loss the fight against boss name 

-Player Movement Method- Lensa
   This method lets the player move around different parts of the game world, making it easier to explore and interact with things.
-Args:
   Player: The Player object that represents the current player.
   Direction: A string that tells which way the player wants to go.
-Returns:
   A string that tells the player where they are now or says if they can't move that way.
-Side Effects:
    Changes the player's current location.
    Shows a message about the movement and what's around the new spot


