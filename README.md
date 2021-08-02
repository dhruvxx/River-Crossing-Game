From lines 1-18
The screen size,caption for the game, background image, and the timer has been specified. Libraries have been imported and pygame has been initialised.

From 20-22
The variables have been initialised

From 25-46
The classes for the player, fixed and moving obstacle has been defined. 
Later is the function which says what to do when either of the player wins. 
Function bye and welcome is to declare the winning and the losing player.
Score function is to display the score.
next_turn function is to refresh the entire game that is to start the game again after the result(winning and the losing player)
Globally declared functions are score1, score2 and seconds
score1 gives the score of player1, score2 of player2 and seconds variable stores the timer value.

The tile classes are for the partitions.
xlist and ylist gives the intial coordinates for the moving obstacles.

Lines 281-284
Gives the for loop to quit the game 

Lines 287-305
Gives the functions of the pressed keys. This moves the player in the required(key we pressed) direction.

Lines 309-328
Calculates the score

Lines 333-342
Interchanges the START and END of the players. the START of player1 is the END of player2 and vice-versa.

Lines 352 and 353
Collisions between the obstacles and the players

Line 359 gives the varible seconds the value of the timer.
Lines 366 and 367 displays the scores of the players.

Lines 369-391
First for loop talks about the conditions for when the player collides with the fixed obstacle. Turn variable checks if the player is 1 or 2 and changes to the other. The level is increased and if all the levels are played, the winner is declared and you quit the game else you refresh the whole game and play for the next player.
Similarly for when player hits the moving obstacles.

Lines 394-419
If it is player1 playing then it starts from the bottom of the screen. Score pf player1 is displayes and the game should now be played by player2 or else the level is increased. Winner is declared after all the levels and that's the end. you move out/ the game has ended else you refresh the whole game and play for the next player.
Similarly for player2.

The code is also updated frequently.