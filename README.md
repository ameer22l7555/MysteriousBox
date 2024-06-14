# MysteriousBox

**Mystery Box Game in Python Using Tkinter**

This Python script implements a simple game called "Mystery Box Game" using the Tkinter library for creating a graphical user interface (GUI). The game is designed to simulate a game where players take turns opening mystery boxes, and the goal is to avoid opening the box containing a "Suicide" message.

**Game Overview**
The game starts with two players, "Player 1" and "Player 2." Each player takes turns clicking on a mystery box. The boxes are initially labeled with a question mark (?). When a player clicks on a box, the box's contents are revealed. If the box contains the "Suicide" message, the game ends, and the player who opened the box loses. If the box is empty, the player's turn ends, and the next player takes their turn.

**Game Logic**
The game logic is implemented in the MysteryBoxGame class. This class initializes the game by setting up the GUI, creating the mystery boxes, and starting the game. The game is controlled by various methods, such as reveal_box, switch_player, and reset_game.

**GUI Components**
The GUI consists of the following components:
**Turn Label**: Displays the current player's turn.
**Boxes Buttons**: A list of buttons representing the mystery boxes.
**Prize Position**: The position of the "Suicide" box in the list of boxes.
**Boxes**: A list of strings representing the contents of the boxes.

**Game Flow**
**Initialization**: The game initializes by setting up the GUI and creating the mystery boxes.
**Game Start**: The game starts by resetting the game, selecting a random position for the "Suicide" box, and shuffling the contents of the boxes.
**Player Turn**: The current player takes their turn by clicking on a mystery box.
**Box Reveal**: The contents of the box are revealed. If the box contains "Suicide," the game ends. If the box is empty, the player's turn ends, and the next player takes their turn.
**Player Switch**: The current player is switched to the next player.
**Turn Update**: The turn label is updated to display the current player.
**Game End**: If the "Suicide" box is opened, the game ends, and the player who opened the box loses. If the player chooses to play again, the game restarts. If not, the game ends.

**Requirements to Run the Code:**
Python Version: The code is written in Python 3.x and should run on any version of Python 3.6 or later.

How to Run the Code:
Save the Code: Save the code in a file named "MysteryBoxGame.py".
Run the Code: Open a terminal or command prompt and navigate to the directory where you saved the file. Run the code using the command 
  
    python MysteryBoxGame.py.

Launch the Game: The game will launch in a new window. You can play the game by clicking on the mystery boxes.

**Conclusion**
The Mystery Box Game is a simple and fun game that can be played by two players. The game demonstrates how to create a GUI game with Tkinter and implement game logic using Python.
