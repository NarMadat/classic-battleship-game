import numpy as np

BOARD_SIZE = 10

def in_bounds(r: int, c: int) -> bool:
    return 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE

def neighbors8(r: int, c: int):
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc

def validate_ship_shape(coords, size: int) -> bool:
    if len(coords) != size:
        return False

    if len(set(coords)) != size:
        return False

    rows = [r for r, _ in coords]
    cols = [c for _, c in coords]

    same_row = len(set(rows)) == 1
    same_col = len(set(cols)) == 1

    if not (same_row or same_col):
        return False

    if same_row:
        r = rows[0]
        sorted_cols = sorted(cols)
        for i in range(1, len(sorted_cols)):
            if sorted_cols[i] - sorted_cols[i-1] != 1:
                return False

        return all(in_bounds(r, c) for c in sorted_cols)

    if same_col:
        c = cols[0]
        sorted_rows = sorted(rows)
        for i in range(1, len(sorted_rows)):
            if sorted_rows[i] - sorted_rows[i-1] != 1:
                return False
        return all(in_bounds(r, c) for r in sorted_rows)

    return False

def can_place_ship(board: np.ndarray, coords) -> bool:
    coords_set = set(coords)

    for r, c in coords:
        if not in_bounds(r, c):
            return False
        if board[r, c] != 0:
            return False

    return True

def place_ship(board: np.ndarray, coords):
    for r, c in coords:
        board[r, c] = 1
