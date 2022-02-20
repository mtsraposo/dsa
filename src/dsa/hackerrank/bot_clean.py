import re
import random

ALL_MOVES = {'UP': (-1, 0),
             'DOWN': (1, 0),
             'RIGHT': (0, 1),
             'LEFT': (0, -1)}


def find_all_dirty_cells(board):
    d_cells = []
    for r in board:
        for c in r:
            if c == 'd':
                d_cells += [(board.index(r), r.index(c))]
    return d_cells


def calc_distances_to_cells(posr, posc, d_cells):
    return sum([abs(posr - d[0]) + abs(posc - d[1]) for d in d_cells])


def find_available_moves(posr, posc, n):
    return {k: v for k, v in ALL_MOVES.items() if (0 <= posr + v[0] < n and 0 <= posc + v[1] < n)}


def calc_distances_after_moves(posr, posc, d_cells, moves):
    return {name: calc_distances_to_cells(*(posr + m[0], posc + m[1]), d_cells) for name, m in moves.items()}


def find_move_to_lowest_distance(posr, posc, move_to_dist, board):
    moves_to_dirty = [m for m in move_to_dist.keys()
                      if board[posr + ALL_MOVES[m][0]][posc + ALL_MOVES[m][1]] == 'd']
    if len(moves_to_dirty) >= 1:
        return moves_to_dirty[random.randint(0, len(moves_to_dirty) - 1)]
    else:
        moves = [k for k, v in move_to_dist.items() if v == min(move_to_dist.values())]
        if len(moves) >= 1:
            return moves[random.randint(0, len(moves) - 1)]
        else:
            return moves[0]



def next_move(posr, posc, board):
    d_cells = find_all_dirty_cells(board)
    if board[posr][posc] == 'd':
        move = 'CLEAN'
    else:
        moves = find_available_moves(posr, posc, len(board))
        move_to_dist = calc_distances_after_moves(posr, posc, d_cells, moves)
        move = find_move_to_lowest_distance(posr, posc, move_to_dist, board)
    print(move)
    return move


def udpate_board(posr, posc, board, move):
    if move == 'CLEAN':
        new_row = f'{board[posr][:posc]}-{board[posr][posc + 1:]}'
        board[posr] = new_row
    else:
        posr, posc = posr + ALL_MOVES[move][0], posc + ALL_MOVES[move][1]
    return posr, posc, board


if __name__ == '__main__':
    # -- Inputs --
    s = """bd---
           -d---
           ---d-
           ---d-
           --d-d"""
    s = re.sub('[ \t]*', '', s)
    board = []
    [board.append(r) for r in s.split('\n')]
    posr, posc = 1, 1

    iter = 0
    MAX_ITER = 50
    while len(find_all_dirty_cells(board)) > 0 and iter < MAX_ITER:
        n_move = next_move(posr, posc, board)
        posr, posc, board = udpate_board(posr, posc, board, n_move)
        print(posr, posc, board)
        iter += 1
    print(iter)
