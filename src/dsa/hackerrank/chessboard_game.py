def gen_eligible_moves(x, y):
    moves = [(x + 1, y - 2), (x - 1, y - 2),
             (x - 2, y - 1), (x - 2, y + 1)]
    moves = list(filter(lambda t: 1 <= t[0] <= 15 and 1 <= t[1] <= 15, moves))
    return moves


def get_layer_coords(x, y):
    return {'layer': max(x, y) - 1,
            'height': min(x, y) - 1}


def is_winning_pos(x, y, pos_layer):
    losing_moves = 0
    outer_moves = []
    moves = gen_eligible_moves(x, y)
    for move in moves:
        layer_coords = get_layer_coords(*move)
        if layer_coords['layer'] < len(pos_layer):
            if pos_layer[layer_coords['layer']][layer_coords['height']] == 0:
                return 1
            else:
                losing_moves += 1
        else:
            outer_moves += [layer_coords]
    if losing_moves == len(moves):
        return 0
    else:
        return abs(1 - is_winning_pos(outer_moves[0]['height'] + 1, outer_moves[0]['layer'] + 1,
                                      pos_layer))


def gen_results_by_pos():
    layers = [[0],
              [0, 0]]
    for c in range(3, 16):
        layers += [[]]
        for r in range(1, c + 1):
            layers[c - 1] += [is_winning_pos(r, c, layers)]
    return layers


x, y = 5, 3
layers = gen_results_by_pos()
layer_coords = get_layer_coords(x, y)
result = layers[layer_coords['layer']][layer_coords['height']]
print('First' if result == 1 else 'Second')
