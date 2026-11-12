import numpy as np

def get_neighbors(r: int, c:int, N: int) -> list:
    neighbors = [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]
    valid_neighbors = []
    for (i,j) in neighbors:
        if i>=0 and i<N and j>=0 and j<N:
            valid_neighbors.append((i,j))
    return valid_neighbors

def go_group_liberties(board: list, row: int, col: int) -> tuple:
    """
    Returns: a tuple of two sorted coordinate lists: group and liberties.
    """
    stone_color = board[row][col]
    N = len(board)
    group = {(row, col)}
    liberties = set()
    stack = [(row, col)]
    while len(stack) >0:
        curr_r, curr_c = stack.pop(0)
        neighbors = get_neighbors(curr_r, curr_c, N)
        for (nei_r, nei_c) in neighbors:
            if board[nei_r][nei_c] == 0:
                liberties.add((nei_r, nei_c))
            elif board[nei_r][nei_c] == stone_color and (nei_r, nei_c) not in group:
                group.add((nei_r, nei_c))
                stack.append((nei_r, nei_c))
    return (sorted(group), sorted(liberties))
        
