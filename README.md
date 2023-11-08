# Number Sum Game with Minimax AI

This Python program implements a console-based Number Sum game where you, as the player, face off against an AI opponent that utilizes the Minimax algorithm to make intelligent moves. This README provides an overview of the game, its components, and how to play it.

## Table of Contents

1. [Introduction](#introduction)
2. [Game Rules](#game-rules)
3. [How to Play](#how-to-play)
4. [Minimax Algorithm](#minimax-algorithm)
5. [Code Structure](#code-structure)
6. [Prerequisites](#prerequisites)
7. [Getting Started](#getting-started)
8. [Contributing](#contributing)

## Introduction

The Number Sum game is a unique mathematical challenge where the objective is to select numbers from a list in such a way that they add up to a specific target value (in this case, 15). This Python implementation creates a list of numbers from 1 to 9, and you play as a human, while the AI opponent plays as the computer. The game ends when either a player successfully forms a combination of numbers that sums up to 15 or when the list is exhausted.

## Game Rules

The rules for this Number Sum game are as follows:

- The game begins with a list of numbers from 1 to 9.
- You, the human player, take the first turn.
- You and the computer take alternating turns selecting a number from the available choices.
- The goal is to select numbers such that their sum equals 15.
- You win the game if you manage to pick numbers that sum up to 15 before the computer does.
- If all the numbers have been chosen, and no player has won, the game ends in a draw.

## How to Play

To play the game, follow these steps:

1. Run the Python program, and you will see a list of available numbers in the console.
2. Enter a number of your choice (between 1 and 9) when prompted. Make sure it's available in the list.
3. The computer will take its turn, making use of the Minimax algorithm to select its move.
4. Continue taking turns until a player wins by forming a sum of 15 or the game ends in a draw.

Remember, you need to achieve a sum of 15 with your chosen numbers to win. Good luck!

## Minimax Algorithm

The AI opponent (the computer) uses the Minimax algorithm to determine the best move it can make. Minimax is a decision-making algorithm used in two-player games to minimize the possible loss for a worst-case scenario. In this game, the computer attempts to maximize its chances of winning while minimizing the chances of the human player winning.

The Minimax algorithm operates as follows:

- It evaluates the current state of the board to see if a player has already won by forming a sum of 15.
- If no player has won yet, it generates all possible moves for both the human and computer players.
- For each move, it recursively evaluates the potential outcomes by simulating the entire game.
- The computer selects the move with the highest likelihood of leading to a win and the lowest likelihood of leading to a loss.

This makes the AI opponent a challenging adversary that can make intelligent decisions throughout the game.

## Code Structure

The code is organized into a `Game` class that contains all the game logic. Here's a brief overview of the key components:

- `Game` class:
  - `__init__`: Initializes the game state, including the list of available numbers and player picks.
  - `evaluate`: A static method to check if a player has won by forming a sum of 15 with their selected numbers.
  - `minimax`: The Minimax algorithm implementation to determine the best move for the computer.
  - `find_best_move`: Utilizes the Minimax algorithm to find the best move for the computer.
  - `play`: The main game loop that allows you to play against the computer.

## Prerequisites

To run the game, you need Python installed on your computer. You can download and install Python from the [official website](https://www.python.org/).

## Getting Started

To play the game, follow these steps:

1. Download the Python code from this repository.
2. Open a terminal or command prompt.
3. Navigate to the directory where the Python file is located.
4. Run the game by executing the following command:

```python
python main.py
