import numpy as np

def validate_pos(pos:tuple, N:int) -> bool:
    i, j = pos
    if i<0 or j<0 or i>=N or j>=N:
        return False
    else:
        return True

def get_neighbors(r:int, c:int, N:int):
    left, right, up, down = (r, c-1), (r, c+1), (r-1, c), (r+1, c)
    neighbors_list = []
    for pos in [left, right, up, down]:
        if validate_pos(pos, N):
            neighbors_list.append(pos)
    return neighbors_list

def find_group(r:int, c:int, N:int, board:list, visited:set, group:list, color: int):
    neighbors = get_neighbors(r, c, N)
    for neighbor in neighbors:
        n_r, n_c = neighbor
        if board[n_r][n_c] == color and neighbor not in visited:
            group.append(neighbor)
            visited.add(neighbor)
            find_group(n_r, n_c, N, board, visited, group, color)
    return group
    
    

def go_group_liberties(board: list, row: int, col: int) -> tuple:
    """
    Returns: a tuple of two sorted coordinate lists: group and liberties.
    """
    stone_color = board[row][col]
    stone_group = list[(row, col)]
    N = len(board)
    group = find_group(row, col, N, board, {(row, col)}, [(row, col)], stone_color)

    liberties = set()
    for group_mem in group:
        g_r, g_c = group_mem
        neighbors = get_neighbors(g_r, g_c, N)
        for n_r, n_c in neighbors:
            if board[n_r][n_c] == 0:
                liberties.add((n_r, n_c))
        
    return (sorted(group), sorted(list(liberties)))
