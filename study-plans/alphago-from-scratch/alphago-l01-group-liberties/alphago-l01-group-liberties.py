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

# claude suggested this function as a hybrid between my previous one and ref solution
def go_group_liberties(board, row, col):
    grid = np.asarray(board)
    N = grid.shape[0]
    colour = grid[row, col]
    group, liberties = {(row, col)}, set()
    stack = [(row, col)]

    while stack:
        r, c = stack.pop()
        for nr, nc in get_neighbors(r, c, N):
            if grid[nr, nc] == 0:
                liberties.add((nr, nc))
            elif grid[nr, nc] == colour and (nr, nc) not in group:
                group.add((nr, nc))          # mark at push time, so no duplicates
                stack.append((nr, nc))

    return sorted(group), sorted(liberties)
