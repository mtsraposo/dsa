from collections import deque
import itertools


def positions_map(bounds):
    return {0: [[bounds[0][0], bounds[0][1]], [bounds[1][0], bounds[1][0] + 1]],
            1: [[bounds[0][1] - 1, bounds[0][1]], [bounds[1][0] + 1, bounds[1][1]]],
            2: [[bounds[0][1] - 1, bounds[0][0]], [bounds[1][1] - 1, bounds[1][1]]],
            3: [[bounds[0][0], bounds[0][0] + 1], [bounds[1][1] - 1, bounds[1][0] + 1]]}


def extend_deque(dq, matrix, bounds, i):
    pos = positions_map(bounds)[i % 4]
    row_range = range(pos[0][0], pos[0][1]) if pos[0][0] < pos[0][1] else reversed(range(pos[0][1], pos[0][0]))
    for r in row_range:
        curr_dq = (matrix[r][pos[1][0]:pos[1][1]]
                   if pos[1][0] < pos[1][1]
                   else list(reversed(matrix[r][pos[1][1]:pos[1][0]])))
        dq[i // 4].extend(curr_dq)


def update_bounds(bounds, i):
    if (i + 1) % 4 == 0 and i != 0:
        bounds[0][0] += 1
        bounds[0][1] -= 1
        bounds[1][0] += 1
        bounds[1][1] -= 1
    return bounds


def rotate_deques(dq, r):
    for i in range(len(dq)):
        dq[i].rotate(r % len(dq[i]))


def reassign_matrix(dq, matrix, layers):
    bounds = [[0, m], [0, n]]  # upper_row, lower_row, left_col, right_col
    dq_pos = 0
    for i in range(layers * 4):
        pos = positions_map(bounds)[i % 4]
        row_range = range(pos[0][0], pos[0][1]) if pos[0][0] < pos[0][1] else reversed(range(pos[0][1], pos[0][0]))
        for r in row_range:
            col_slice = slice(pos[1][0], pos[1][1]) if pos[1][0] < pos[1][1] else slice(pos[1][1], pos[1][0])
            dq_size = abs(pos[1][1] - pos[1][0])
            dq_slice = list(itertools.islice(dq[i // 4], dq_pos, dq_pos + dq_size))
            matrix[r][col_slice] = dq_slice if pos[1][0] < pos[1][1] else list(reversed(dq_slice))
            dq_pos += dq_size
        bounds = update_bounds(bounds, i)
        dq_pos = 0 if (i + 1) % 4 == 0 else dq_pos


def matrixRotation(matrix, m, n, r):
    layers = min(m, n) // 2
    dq = [deque() for _ in range(layers)]
    bounds = [[0, m], [0, n]]  # upper_row, lower_row, left_col, right_col
    for i in range(layers * 4):
        extend_deque(dq, matrix, bounds, i)
        bounds = update_bounds(bounds, i)
    rotate_deques(dq, r)
    reassign_matrix(dq, matrix, layers)
    [print(' '.join(list(map(str, matrix[r])))) for r in range(m)]


if __name__ == "__main__":
    s = """5 4 7
            1 2 3 4
            7 8 9 10
            13 14 15 16
            19 20 21 22
            25 26 27 28"""
    input_string = s.split('\n')
    dimensions = input_string[0].rsplit()
    m, n, r = int(dimensions[0]), int(dimensions[1]), int(dimensions[2])
    matrix = [list(map(int, input_string[i].rsplit())) for i in range(1, m + 1)]

    matrixRotation(matrix, m, n, r)
