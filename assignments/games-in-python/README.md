
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a playable Hangman game in Python. Practice string manipulation, loops, conditionals, user input, and random selection while tracking the player's progress and remaining attempts.

## 📝 Tasks

### 🛠️ Set Up the Game State

#### Description

Complete the setup code so the game randomly selects a secret word and prepares the variables needed to track the player's guesses.

#### Requirements

Completed program should:

- Select one word at random from the provided `words` list.
- Initialize a collection for the letters the player has guessed.
- Initialize a counter for incorrect guesses.
- Set a maximum number of incorrect guesses before the game ends.

### 🛠️ Implement the Guessing Game

#### Description

Complete the main game loop so the player can guess letters, see their progress, and receive a win or lose result.

#### Requirements

Completed program should:

- Display the hidden word as underscores and reveal letters after they are guessed.
- Ask the player for a letter and record each guess.
- Update the incorrect guess count when the guessed letter is not in the secret word.
- End when the player reveals the entire word or reaches the maximum number of incorrect guesses.
- Display a clear win message or reveal the secret word in a lose message.
