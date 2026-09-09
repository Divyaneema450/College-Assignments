# Tic-Tac-Toe Game

## Assignment No. 3

### Title
Write a program to implement Tic-Tac-Toe game.

## Problem Statement

Write a program to implement a CLI-based Tic-Tac-Toe game using Python.

## Objective

The objective of this assignment is to implement a two-player Tic-Tac-Toe game using a 3 × 3 board. The program allows players X and O to take turns, checks for winning conditions, and detects a draw.

## Features

- 3 × 3 game board
- Two-player gameplay
- Player X starts the game
- Player O plays after X
- Row, column and diagonal win detection
- Draw detection
- Invalid move handling
- Command-line interface

## Algorithm

1. Create a 3 × 3 board and initialize all cells with `-`.
2. Display the current board.
3. Set Player X as the first player.
4. Ask the current player to enter the row and column.
5. Validate the entered move.
6. Place the player's symbol on the board.
7. Check all rows, columns and diagonals for a winning condition.
8. If the player wins, display the winning message and end the game.
9. Check whether the board is completely filled.
10. If the board is full, display the draw message.
11. Switch the current player between X and O.
12. Continue until a player wins or the game ends in a draw.

## Functions

### `initialize_board()`
Creates an empty 3 × 3 Tic-Tac-Toe board.

### `display_board(board)`
Displays the current board on the screen.

### `check_win(board, player)`
Checks whether the specified player has three symbols in a row, column, or diagonal.

### `check_draw(board)`
Checks whether all cells of the board are filled.

### `player_move(board, player)`
Takes input from the player and validates the selected position.

### `play_tic_tac_toe()`
Controls the complete game.

## How to Run

Make sure Python 3 is installed.

Run the program using:

```bash
python tic_tac_toe.py
