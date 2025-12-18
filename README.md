# Battleship (Console Version)

This project is a simplified console implementation of the classic Battleship game.
The game is fully playable from the terminal and follows all standard placement
and gameplay rules.

---

## Input Format

Player ship placement is done manually through the terminal.
For each ship, the player enters its coordinates cell by cell.

Each coordinate is entered in the format:

row col

Where:
- `row` and `col` are integers from 0 to 9
- the board size is 10×10

For example, a ship of size 3 can be entered as:
0 0  
0 1  
0 2  

This simple numeric format was chosen to minimize parsing complexity
and reduce input errors.

---

## Ship Placement Validation

Ship placement is validated according to the classic Battleship rules:

- The number of entered cells must match the required ship size
- All ship cells must lie inside the 10×10 board
- Ships must be placed in a straight line (horizontal or vertical)
- Ship cells must be contiguous, without gaps
- Ships must not overlap
- Ships must not touch each other, even diagonally

The game board is stored as a 10×10 NumPy array, which allows efficient
neighbor and boundary checks during validation.

---

## Game State Update and Display

The game state is updated after every move.

- Shots are tracked on separate 10×10 boards for the player and the bot
- Each cell can be in one of three states:
  - Unknown
  - Hit
  - Miss

After each move:
- The game state is saved to `data/game_state.csv`
- A visual representation of both boards is printed to the terminal

The board is displayed using simple ASCII symbols:
- `.` for unknown cells
- `X` for hits
- `o` for misses

When a ship is fully destroyed, all surrounding cells (including diagonals)
are automatically marked as misses, as required by the rules.

---

## Design Decisions and Trade-offs

- The game is implemented as a console application without graphical libraries,
  focusing on logic and correctness rather than visuals.
- NumPy arrays are used to represent the game board for simplicity and performance.
- Ship data for both the player and the bot is stored in CSV format using pandas,
  allowing easy inspection and compatibility between components.
- The same validation logic is reused for both player input and bot ship generation
  to avoid duplicated code and ensure consistent rules.
- The bot AI is intentionally kept simple to match the educational scope of the project.

---

## Running the Project

Create and activate a virtual environment, then install dependencies:

python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  
python main.py
