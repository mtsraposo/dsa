class ConnectedNode:
    def __init__(self, value, coords):
        self.connections = [coords]
        self.value = value
        self.coords = coords
        self.visited = False
        self.cluster_size = value

    def add_connection(self, connection_coords):
        self.connections += [connection_coords]


def gen_neighborhood_bounds(i, j, rows, cols):
    return {'row': {'start': max(0, i - 1),
                    'end': min(rows - 1, i + 1) + 1},
            'col': {'start': max(0, j - 1),
                    'end': min(cols - 1, j + 1) + 1}}


def update_neighbors(matrix, bounds, i, j):
    if matrix[i][j].value == 1:
        for r in range(bounds['row']['start'], bounds['row']['end']):
            for c in range(bounds['col']['start'], bounds['col']['end']):
                if not isinstance(matrix[r][c], ConnectedNode):
                    matrix[r][c] = ConnectedNode(matrix[r][c], (r, c))
                else:
                    if matrix[r][c].value == 1 and (matrix[r][c].coords not in matrix[i][j].connections):
                        matrix[i][j].add_connection(matrix[r][c].coords)
                        matrix[r][c].add_connection(matrix[i][j].coords)
    return matrix


def find_max_connected_cluster(linked_matrix, rows, cols):
    max_connections = 0
    for i in range(rows):
        for j in range(cols):
            linked_matrix[i][j].visited = True
            if linked_matrix[i][j].value == 1:
                if len(linked_matrix[i][j].connections) == 2:
                    (r, c) = linked_matrix[i][j].connections[1]
                    if linked_matrix[r][c].cluster_size > 1:
                        if linked_matrix[i][j].cluster_size == 1:
                            linked_matrix[i][j].cluster_size += linked_matrix[r][c].cluster_size
                            linked_matrix[r][c].cluster_size = linked_matrix[i][j].cluster_size
                        else:
                            linked_matrix[i][j].cluster_size = max(linked_matrix[r][c].cluster_size,
                                                                   linked_matrix[i][j].cluster_size)
                            linked_matrix[r][c].cluster_size = linked_matrix[i][j].cluster_size
                else:
                    for (r, c) in linked_matrix[i][j].connections:
                        visited = linked_matrix[r][c].visited
                        equals_one = linked_matrix[r][c].value == 1
                        if not visited and equals_one:
                            linked_matrix[i][j].cluster_size += 1
                    for (r, c) in linked_matrix[i][j].connections:
                        if linked_matrix[r][c].cluster_size >= 1:
                            linked_matrix[r][c].cluster_size = linked_matrix[i][j].cluster_size
                            linked_matrix[r][c].visited = True
            if linked_matrix[i][j].cluster_size > max_connections:
                max_connections = linked_matrix[i][j].cluster_size
            print(f'-----({i}, {j})-----')
            for m in range(rows):
                print([linked_matrix[m][n].cluster_size for n in range(cols)])
    return max_connections


def connected_cell(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if not isinstance(matrix[i][j], ConnectedNode):
                matrix[i][j] = ConnectedNode(matrix[i][j], (i, j))
            neighborhood_bounds = gen_neighborhood_bounds(i, j, rows, cols)
            update_neighbors(matrix, neighborhood_bounds, i, j)
    return matrix


linked_matrix = connected_cell(matrix=[[0, 1, 1, 1, 1],
                                       [1, 0, 0, 0, 1],
                                       [1, 1, 0, 1, 0],
                                       [0, 1, 0, 1, 1],
                                       [0, 1, 1, 1, 0]])
rows = len(linked_matrix)
cols = len(linked_matrix[0])
tmp = find_max_connected_cluster(linked_matrix, rows, cols)
