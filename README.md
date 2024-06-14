# MysteriousBox


MysteriousBox.py
This Python file contains the implementation of a simple and interactive "Mystery Box Game" using the tkinter library for GUI elements. Below is a detailed description of the file's functionality:

Description
MysteryBoxGame Class:

Initialization (__init__):

Sets up the main window with a title "Mystery Box Game" and a background color.
Initializes 20 boxes (buttons) and two players.
Displays a label indicating the current player's turn.
Calls methods to create buttons and start the game.
create_buttons:

Creates 20 buttons arranged in a grid (5x4).
Each button is initially labeled with a "?" and is clickable to reveal its content.
start_game:

Resets the game to its initial state.
Randomly assigns one box as the "Suicide" box.
Shuffles the boxes to randomize their positions.
reveal_box:

Handles the logic when a box is clicked.
If the clicked box contains "Suicide", the current player loses, and a message box displays the result.
If the box is empty, it switches the turn to the other player and updates the turn label.
switch_player:

Switches the turn between Player 1 and Player 2.
update_turn_label:

Updates the label to show the current player's turn.
reset_game:

Resets all buttons to their initial state (labeled "?" and enabled).
Resets the turn to Player 1.
ask_play_again:

Prompts the player with a message box to play again or quit the game.
Restarts the game if the player chooses to play again, otherwise closes the application.
Main Function (main):

Initializes the tkinter main loop and creates an instance of the MysteryBoxGame class.
Execution:

The game starts when the script is run directly.
Usage
To play the game, run the script. Click on the boxes to reveal whether they are empty or contain the "Suicide" label. The game alternates turns between two players. If a player clicks the "Suicide" box, they lose the game, and a prompt will ask if they want to play again.

    python MysteriousBox.py


This script provides a fun and simple way to test your luck with friends. Enjoy the game!
