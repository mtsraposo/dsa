def forming_magic_square(s):
    """
    There are only 4 possibilities to form a 3x3 magic square, and all of them
    are rotations of the others and have a 5 at their centers.
    """
    center_cost = abs(s[1][1] - 5)  # Center cost may be calculated directly

    # -- Search corner rotation that minimizes cost

    corners = [s[0][0], s[0][2], s[2][2], s[2][0]]  # Clockwise corner values
    magic_corners = [8, 4, 2, 6]  # Clockwise magic square corner values
    magic_corner_rotations = [magic_corners[-i:] + magic_corners[:-i] for i in range(len(magic_corners))]

    corner_cost = 36
    magic_rotation = 2
    for index, mc in enumerate(magic_corner_rotations):
        cost = sum([abs(mc[i] - corners[i]) for i in range(len(mc))])
        corner_cost = min(cost, corner_cost)
        magic_rotation = index if cost == corner_cost else magic_rotation

    # -- Given a magic_setting, calculate the cost to convert the edges

    edges = [s[0][1], s[1][2], s[2][1], s[1][0]]  # Clockwise edge values
    magic_edges = [3, 9, 7, 1]  # Clockwise magic square edge values
    magic_edge_rotations = [magic_edges[-i:] + magic_edges[:-i] for i in range(len(magic_edges))]
    me = magic_edge_rotations[magic_rotation]
    edge_cost = sum([abs(me[i] - edges[i]) for i in range(len(me))])

    return center_cost + corner_cost + edge_cost


if __name__ == '__main__':
    s = [[5, 3, 4],
         [1, 5, 8],
         [6, 4, 2]]

    print(forming_magic_square(s))
