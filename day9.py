def main():
    # https://adventofcode.com/2021/day/9
    print("Starting...")

    with open("inputs/day_9_input.txt", 'r') as infile:
        lines = infile.readlines()

    matrix = parse_file(lines)
    print(matrix)

    # for part I
    # risk = calculate_risk_level(matrix)
    # print("Risk: {}".format(risk))

    # for part II
    basins = find_basins(matrix)
    basin_sizes = sorted([len(basin) for basin in basins])
    score = basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]
    print("Score: {}".format(score))

    print("Done!")


def parse_file(lines):
    rows = []
    for line in lines:
        row = [int(digit) for digit in line.strip()]
        rows.append(row)
    return rows


def calculate_risk_level(matrix):
    risk = 0
    width = len(matrix)
    height = len(matrix[0])
    for r in range(width):
        for c in range(height):
            if lower_than_adj(r, c, matrix):
                risk += matrix[r][c] + 1
    return risk


def find_basins(matrix):
    basins = []

    width = len(matrix)
    height = len(matrix[0])
    for r in range(width):
        for c in range(height):
            if lower_than_adj(r, c, matrix):
                basin = find_basin(r, c, matrix)
                basins.append(basin)

    return basins


# basic breadth-first search to find nodes
def find_basin(row, col, matrix):
    queue = set()
    visited = set()

    # init queue with starting node
    queue.add((row, col))

    while queue:
        r, c = queue.pop()
        # get the adjacent nodes that are not 9 for the basin
        adj_list = get_adj_basin(r, c, matrix)
        for adj in adj_list:
            if adj not in visited:
                queue.add(adj)
        visited.add((r, c))

    return visited


def get_adj_basin(row, col, matrix):
    adj = []
    width = len(matrix)
    height = len(matrix[0])

    # top
    if col - 1 >= 0 and matrix[row][col - 1] != 9:
        adj.append((row, col - 1))

    # bot
    if col + 1 < height and matrix[row][col + 1] != 9:
        adj.append((row, col + 1))

    # left
    if row - 1 >= 0 and matrix[row - 1][col] != 9:
        adj.append((row - 1, col))

    # right
    if row + 1 < width and matrix[row + 1][col] != 9:
        adj.append((row + 1, col))

    return adj


def lower_than_adj(row, col, matrix):
    value = matrix[row][col]
    # print("({},{}): {}".format(row, col, value))
    # ignore diags for part I
    width = len(matrix)
    height = len(matrix[0])

    # top
    if col - 1 >= 0:
        top = matrix[row][col - 1]
        if value >= top:
            return False

    # bot
    if col + 1 < height:
        bot = matrix[row][col + 1]
        if value >= bot:
            return False

    # left
    if row - 1 >= 0:
        left = matrix[row - 1][col]
        if value >= left:
            return False

    # right
    if row + 1 < width:
        right = matrix[row + 1][col]
        if value >= right:
            return False

    return True


if __name__ == '__main__':
    main()
