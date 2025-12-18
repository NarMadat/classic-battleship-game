import numpy as np
import pandas as pd
import random
from src.utils import BOARD_SIZE, neighbors8
from src.logger import LOGGER

def shoot(target_board, shots_board, r, c):
    if shots_board[r, c] != 0:
        LOGGER.debug("Ignoring repeated shot at (%d, %d).", r, c)
        return None

    if target_board[r, c] == 1:
        shots_board[r, c] = 2
        LOGGER.info("Hit registered at (%d, %d).", r, c)
        return True
    else:
        shots_board[r, c] = -1
        LOGGER.debug("Miss recorded at (%d, %d).", r, c)
        return False

def is_ship_destroyed(ship_coords, shots_board):
    for r, c in ship_coords:
        if shots_board[r, c] != 2:
            return False
    LOGGER.info("Ship destroyed at coordinates: %s", ship_coords)
    return True

def save_game_state(path, data):
    LOGGER.info("Saving game state to %s", path)
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)
