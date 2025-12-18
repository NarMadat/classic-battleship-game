import numpy as np
import pandas as pd
import random
from src.utils import BOARD_SIZE, neighbors8

def shoot(target_board, shots_board, r, c):
    if shots_board[r, c] != 0:
        return None

    if target_board[r, c] == 1:
        shots_board[r, c] = 2
        return True
    else:
        shots_board[r, c] = -1
        return False

def is_ship_destroyed(ship_coords, shots_board):
    for r, c in ship_coords:
        if shots_board[r, c] != 2:
            return False
    return True

def save_game_state(path, data):
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)
