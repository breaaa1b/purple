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
