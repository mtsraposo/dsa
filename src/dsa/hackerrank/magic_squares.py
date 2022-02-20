def gen_rotations(elements):
    return [elements[-i:] + elements[:-i] for i in range(len(elements))]


def gen_all_rotations(elements, reindex):
    rotations = gen_rotations(elements)
    # add reflections relative to the central column
    elements = [elements[i] for i in reindex]
    rotations += gen_rotations(elements)
    return rotations


def calc_magic_rotation_cost(magic_rotation, rotations, elements):
    r = rotations[magic_rotation]
    return sum([abs(r[i] - elements[i]) for i in range(len(r))])


def search_best_rotation(edges, edge_rotations, corners, corner_rotations):
    total_cost = 100
    magic_rotation = 0
    for index, r in enumerate(edge_rotations):
        edge_cost = sum([abs(r[i] - edges[i]) for i in range(len(r))])
        corner_cost = calc_magic_rotation_cost(index, corner_rotations, corners)
        print(edge_cost, corner_cost)
        total_cost = min(edge_cost + corner_cost, total_cost)
        print(total_cost)
        magic_rotation = index if total_cost == edge_cost + corner_cost else magic_rotation
    return total_cost, magic_rotation


def forming_magic_square(s):
    """
    There are only 8 possibilities to form a 3x3 magic square, and all of them
    are rotations or reflections of the others and have a 5 at their centers.
    """
    center_cost = abs(s[1][1] - 5)  # Center cost may be calculated directly

    # -- Define corners and edges, as well as magic rotations

    edges = [s[0][1], s[1][2], s[2][1], s[1][0]]  # Clockwise edge values
    magic_edges = [3, 9, 7, 1]  # Clockwise magic square edge values
    magic_edge_rotations = gen_all_rotations(magic_edges, reindex=[0, 3, 2, 1])

    corners = [s[0][0], s[0][2], s[2][2], s[2][0]]  # Clockwise corner values
    magic_corners = [8, 4, 2, 6]  # Clockwise magic square corner values
    magic_corner_rotations = gen_all_rotations(magic_corners, reindex=[1, 0, 3, 2])

    # -- Search rotation that minimizes cost

    edge_corner_cost = search_best_rotation(edges, magic_edge_rotations, corners, magic_corner_rotations)[0]

    return center_cost + edge_corner_cost


if __name__ == '__main__':
    s = [[4, 5, 8],
         [2, 4, 1],
         [1, 9, 7]]

    print(forming_magic_square(s))
