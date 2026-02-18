# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic Hangman word-guessing game using Python, practicing string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️	Set Up the Game

#### Description
Create the core game structure by defining a word list and implementing the random word selection and initial display logic.

#### Requirements
Completed program should:

- Define a list of at least 10 words for the game to choose from
- Randomly select one word at the start of each game using the `random` module
- Display the word as underscores (e.g., `_ _ _ _`) representing each letter


### 🛠️	Implement the Game Loop

#### Description
Build the main game loop that accepts player guesses, validates input, and updates the game state each turn.

#### Requirements
Completed program should:

- Prompt the player to enter a single letter guess each turn
- Validate that the input is a single alphabetical character
- Reveal correctly guessed letters in their proper positions
- Track and display the number of incorrect guesses remaining (starting from 6)
- Keep track of previously guessed letters and notify the player of duplicates


### 🛠️	Handle Win and Lose Conditions

#### Description
Add logic to detect when the game is over and display an appropriate message to the player.

#### Requirements
Completed program should:

- End the game with a win message when all letters are correctly guessed
- End the game with a lose message when the player runs out of attempts
- Reveal the full word when the player loses
