

def main():
    # https://adventofcode.com/2021/day/13
    print("Starting...")

    with open("inputs/day_13_input.txt", 'r') as infile:
        lines = infile.readlines()

    points, instructions = parse_file(lines)
    print(points)
    print(instructions)

    # for part I
    matrix = create_matrix(points)
    folded = execute_instructions(matrix, [instructions[0]])
    num_points = count_points(folded)
    print("Num Points: {}".format(num_points))

    # for part II
    matrix = create_matrix(points)
    folded = execute_instructions(matrix, instructions)
    for row in folded:
        print(row)
    # spells out AHPRPAUZ

    print("Done!")


def count_points(matrix):
    points = 0
    width = len(matrix)
    height = len(matrix[0])
    for r in range(width):
        for c in range(height):
            if matrix[r][c]:
                points += 1
    return points


def execute_instructions(matrix, instructions):
    for instruction in instructions:
        direction, val = instruction
        if direction == 'y':
            matrix = fold_horizontally(matrix, val)
        elif direction == 'x':
            matrix = fold_vertically(matrix, val)
    return matrix


def fold_vertically(matrix, fold):
    width = len(matrix)
    height = len(matrix[0])
    folded = [[0] * fold for _ in range(width)]
    for r in range(width):
        for c in range(height):
            if c < fold:
                folded[r][c] = matrix[r][c]
            elif c > fold and matrix[r][c]:
                diff = height - 1 - c
                folded[r][diff] = matrix[r][c]
    return folded


def fold_horizontally(matrix, fold):
    width = len(matrix)
    height = len(matrix[0])
    folded = [[0] * height for _ in range(fold)]
    for r in range(width):
        for c in range(height):
            if r < fold:
                folded[r][c] = matrix[r][c]
            elif r > fold and matrix[r][c]:
                diff = width - 1 - r
                folded[diff][c] = matrix[r][c]
    return folded


def create_matrix(points):
    width, height = find_corners(points)
    matrix = [[0] * (width + 1) for _ in range(height + 1)]
    for point in points:
        x, y = point
        matrix[y][x] = 1
    return matrix


def find_corners(points):
    max_width = 0
    max_height = 0
    for point in points:
        x, y = point
        max_width = max(x, max_width)
        max_height = max(y, max_height)
    return max_width, max_height


def parse_file(lines):
    matrix = []
    instructions = []
    seen_space = False
    for line in lines:
        if line == "\n":
            seen_space = True
            continue
        if not seen_space:
            x, y = line.strip().split(',')
            matrix.append((int(x), int(y)))
        else:
            text = line.strip().replace("fold along ", "")
            direction, val = text.split("=")
            instructions.append((direction, int(val)))

    return matrix, instructions


if __name__ == '__main__':
    main()
