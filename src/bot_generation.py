import os
import random
import numpy as np
import pandas as pd

from src.utils import (
    BOARD_SIZE,
    validate_ship_shape,
    can_place_ship,
    place_ship,
)

SHIP_SIZES = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

DIRECTIONS = [
    (0, 1),
    (1, 0),
]

def generate_ship_coords(size: int):
    """
    Randomly generates coordinates for a ship of given size.
    Returns list of (r, c).
    """
    r = random.randint(0, BOARD_SIZE - 1)
    c = random.randint(0, BOARD_SIZE - 1)
    dr, dc = random.choice(DIRECTIONS)

    coords = []
    for i in range(size):
        coords.append((r + dr * i, c + dc * i))
    return coords

def save_ships_to_csv(ships, path: str):
    rows = []
    for ship_id, coords in enumerate(ships):
        for r, c in coords:
            rows.append({"ship_id": ship_id, "row": r, "col": c})
    df = pd.DataFrame(rows)
    df.to_csv(path, index=False)

def generate_bot_ships(output_csv="data/bot_ships.csv"):
    """
    Automatically generates placement for the bot.
    """
    board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
    ships = []

    print("=== Generating bot ships ===")

    for size in SHIP_SIZES:
        while True:
            coords = generate_ship_coords(size)

            if not validate_ship_shape(coords, size):
                continue

            if not can_place_ship(board, coords):
                continue

            place_ship(board, coords)
            ships.append(coords)
            break

    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    save_ships_to_csv(ships, output_csv)

    print(f"✅ Bot ships saved to {output_csv}")

    return board, ships
