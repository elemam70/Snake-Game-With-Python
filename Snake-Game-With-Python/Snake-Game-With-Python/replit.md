# Snake Game

## Overview
A classic snake game built with Python and Pygame. Control the snake with arrow keys, eat food to grow longer, and avoid running into yourself!

## Current State
The game is fully functional with:
- Snake movement using arrow keys (up, down, left, right)
- Food spawning at random positions
- Snake growth when eating food
- Collision detection for self-collision (resets the game)
- Score tracking displayed on screen
- Grid-based retro-style interface

## Recent Changes
- November 15, 2025: Initial project creation
  - Set up Python 3.11 environment
  - Installed Pygame library
  - Created complete snake game with all core features
  - Configured VNC workflow for GUI display

## How to Play
- Use arrow keys to control the snake's direction
- Eat the red food to grow longer and increase your score
- Avoid running into yourself or the game will reset
- The snake wraps around the screen edges

## Project Architecture
- `main.py`: Main game file containing Snake and Food classes
- Game runs at 10 FPS for smooth classic snake gameplay
- 600x600 pixel window with 20x20 pixel grid squares
