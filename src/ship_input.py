import os
import pandas as pd
import numpy as np

from src.utils import BOARD_SIZE, validate_ship_shape, can_place_ship, place_ship
from src.logger import LOGGER

SHIP_SIZES = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

def read_ship_coords(size: int):
    """
    Reads 'size' lines, each line: "row col"
    Returns list of tuples [(r,c),...]
    """
    coords = []
    print(f"\nEnter ship of size {size}. Provide {size} coordinates as: row col (0..9)")
    for i in range(size):
        while True:
            raw = input(f"  cell {i+1}/{size}: ").strip()
            parts = raw.split()
            if len(parts) != 2:
                print("Invalid format. Use: row col")
                continue
            try:
                r = int(parts[0])
                c = int(parts[1])
            except ValueError:
                print("Row and col must be integers.")
                continue
            coords.append((r, c))
            break
    return coords

def save_ships_to_csv(ships, path: str):
    rows = []
    for ship_id, coords in enumerate(ships):
        for r, c in coords:
            rows.append({"ship_id": ship_id, "row": r, "col": c})
    df = pd.DataFrame(rows)
    df.to_csv(path, index=False)

def get_player_ships(output_csv="data/player_ships.csv"):
    """
    Main function for Part 1:
    - asks user to input ships
    - validates ship rules
    - saves to CSV
    Returns: (board, ships)
    """
    board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
    ships = []

    print("=== Player ship placement ===")
    LOGGER.info("Player ship placement initialized; expecting %d ships.", len(SHIP_SIZES))
    print("Board is 10x10 with coordinates row col from 0 to 9.")
    print("Important: ships must NOT touch even diagonally.\n")

    for size in SHIP_SIZES:
        while True:
            coords = read_ship_coords(size)
            LOGGER.debug("Coordinates entered for ship size %d: %s", size, coords)

            if not validate_ship_shape(coords, size):
                LOGGER.warning("Invalid shape provided for ship size %d: %s", size, coords)
                print("❌ Invalid ship shape. Must be straight line and contiguous.")
                print("Example for size 3: (0 0), (0 1), (0 2) or (1 5), (2 5), (3 5)")
                continue

            if not can_place_ship(board, coords):
                LOGGER.warning("Failed placement attempt for ship size %d at %s", size, coords)
                print("❌ Cannot place ship here: out of bounds, overlaps, or touches another ship (even diagonally).")
                continue

            place_ship(board, coords)
            LOGGER.info("Placed ship size %d at %s", size, coords)
            ships.append(coords)
            print("  ✅ Ship placed.")
            break

    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    save_ships_to_csv(ships, output_csv)
    LOGGER.info("All ships saved to %s", output_csv)
    print(f"\n✅ All ships saved to {output_csv}")

    return board, ships
