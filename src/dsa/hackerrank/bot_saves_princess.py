import re


def find_princess(n, grid):
    first_col = [r[0] for r in grid]
    if n == 1:
        return 0, 0
    elif 'p' in grid[0]:
        return 0, grid[0].index('p')
    elif 'p' in first_col:
        return first_col.index('p'), 0
    else:
        princess = find_princess(n - 1, [r[1:] for r in grid[1:]])
        return princess[1] + 1, princess[1] + 1


def next_move(n, r, c, grid):
    p = find_princess(n, grid)
    if p[1] - c < 0:
        return 'LEFT'
    elif p[1] - c > 0:
        return 'RIGHT'
    else:
        if p[0] - r < 0:
            return 'UP'
        else:
            return 'DOWN'


if __name__ == '__main__':
    # -- Inputs --
    s = """-----
            -----
            p--m-
            -----
            -----"""
    s = re.sub('[ \t]*', '', s)
    grid = []
    [grid.append(r) for r in s.split('\n')]
    n = len(grid)
    r, c = 2, 3

    # -- Next move --
    next_move(n, r, c, grid)
