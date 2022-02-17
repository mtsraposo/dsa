class ConnectedNode:
    def __init__(self, value, cluster_id):
        self.value = value
        self.visited = False
        self.cluster_id = cluster_id


def gen_neighborhood_bounds(i, j, rows, cols):
    return {'row': {'start': max(0, i - 1),
                    'end': min(rows - 1, i + 1) + 1},
            'col': {'start': max(0, j - 1),
                    'end': min(cols - 1, j + 1) + 1}}


def search_cluster(matrix, i, j, rows, cols, clusters):
    bounds = gen_neighborhood_bounds(i, j, rows, cols)
    for r in range(bounds['row']['start'], bounds['row']['end']):
        for c in range(bounds['col']['start'], bounds['col']['end']):
            if not isinstance(matrix[r][c], ConnectedNode):
                matrix[r][c] = ConnectedNode(matrix[r][c], None)
            if not matrix[r][c].visited and matrix[r][c].value == 1:
                matrix[r][c].cluster_id = matrix[i][j].cluster_id
                matrix[r][c].visited = True
                clusters[matrix[i][j].cluster_id] += 1
                search_cluster(matrix, r, c, rows, cols, clusters)


def print_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for m in range(rows):
        print([matrix[m][n].cluster_id for n in range(cols)])


def connected_cell(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    cluster_id = 0
    clusters = dict()
    for i in range(rows):
        for j in range(cols):
            if not isinstance(matrix[i][j], ConnectedNode):
                matrix[i][j] = ConnectedNode(matrix[i][j], None)
            if not matrix[i][j].visited and matrix[i][j].value == 1:
                matrix[i][j].cluster_id = cluster_id
                matrix[i][j].visited = True
                clusters[cluster_id] = 1
                search_cluster(matrix, i, j, rows, cols, clusters)
                cluster_id += 1
    print_matrix(matrix)
    return max(clusters.values())


max_cluster = connected_cell(matrix=[[0, 1, 1, 1, 1],
                                       [1, 0, 0, 0, 1],
                                       [1, 1, 0, 1, 0],
                                       [0, 1, 0, 1, 1],
                                       [0, 1, 1, 1, 0]])
