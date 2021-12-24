
def main():
    # https://adventofcode.com/2021/day/5
    print("Starting...")

    with open("inputs/day_5_input.txt", 'r') as infile:
        lines = infile.readlines()

    line_segments = parse_file(lines)
    max_width, max_height = find_corners(line_segments)
    print(max_width, max_height)
    grid = create_empty_grid(max_width, max_height)

    # filter them for part I
    # line_segments = filter_lines(line_segments)
    for line_segment in line_segments:
        write_line(grid, line_segment)

    # too large for big boards
    # for row in grid:
    #     print(row)

    total_int = count_intersections(grid, 2)
    print("Total Intersections > 2 : {}".format(total_int))

    print("Done!")


def parse_file(lines):
    line_segments = []

    for line in lines:
        vals = line.strip().split(" -> ")
        first = [int(digit) for digit in vals[0].strip().split(",")]
        second = [int(digit) for digit in vals[1].strip().split(",")]
        segment = {
            "sx": first[0],
            "sy": first[1],
            "ex": second[0],
            "ey": second[1]
        }
        # how to store?
        line_segments.append(segment)

    # 6,4 -> 2,0

    return line_segments


def filter_lines(lines):
    good_lines = []
    # only keep horizontal and vertical lines
    for line in lines:
        x_diff = line["ex"] - line["sx"]
        y_diff = line["ey"] - line["sy"]
        if x_diff != 0 and y_diff != 0:
            continue
        good_lines.append(line)
    return good_lines


def find_corners(line_segments):
    max_width = 0
    max_height = 0
    for line in line_segments:
        if line["sx"] > max_width:
            max_width = line["sx"]
        if line["ex"] > max_width:
            max_width = line["ex"]
        if line["sy"] > max_height:
            max_height = line["sy"]
        if line["ey"] > max_height:
            max_height = line["ey"]
    return max_width, max_height


def count_intersections(grid, min_int=2):
    num = 0
    for row in grid:
        for val in row:
            if val >= min_int:
                num += 1
    return num


def write_diagonal_line(grid, line):
    # first determine the lines direction
    x_diff = line["ex"] - line["sx"]
    y_diff = line["ey"] - line["sy"]

    xp = line["sx"]
    yp = line["sy"]

    # draw any diagonal lines
    if x_diff >= 1 and y_diff >= 1:
        while xp <= line["ex"] and yp <= line["ey"]:
            grid[yp][xp] = grid[yp][xp] + 1
            xp += 1
            yp += 1
    elif x_diff <= -1 and y_diff <= -1:
        while xp >= line["ex"] and yp >= line["ey"]:
            grid[yp][xp] = grid[yp][xp] + 1
            xp -= 1
            yp -= 1
    elif x_diff >= 1 and y_diff <= -1:
        while xp <= line["ex"] and yp >= line["ey"]:
            grid[yp][xp] = grid[yp][xp] + 1
            xp += 1
            yp -= 1
    elif x_diff <= -1 and y_diff >= 1:
        while xp >= line["ex"] and yp <= line["ey"]:
            grid[yp][xp] = grid[yp][xp] + 1
            xp -= 1
            yp += 1


def write_horizonal_or_vertical_line(grid, line):
    # first determine the lines direction
    x_diff = line["ex"] - line["sx"]
    y_diff = line["ey"] - line["sy"]

    xp = line["sx"]
    yp = line["sy"]

    # now draw the line, only horizontal or diagonal
    if x_diff >= 1:
        while xp <= line["ex"]:
            grid[yp][xp] = grid[yp][xp] + 1
            xp += 1
    elif x_diff <= -1:
        while xp >= line["ex"]:
            grid[yp][xp] = grid[yp][xp] + 1
            xp -= 1
    elif y_diff >= 1:
        while yp <= line["ey"]:
            grid[yp][xp] = grid[yp][xp] + 1
            yp += 1
    elif y_diff <= -1:
        while yp >= line["ey"]:
            grid[yp][xp] = grid[yp][xp] + 1
            yp -= 1


def write_line(grid, line):
    # first determine the lines direction
    x_diff = line["ex"] - line["sx"]
    y_diff = line["ey"] - line["sy"]

    if x_diff != 0 and y_diff != 0:
        write_diagonal_line(grid, line)
    else:
        write_horizonal_or_vertical_line(grid, line)


def create_empty_grid(width, height):
    return [[0] * (height + 1) for _ in range(width + 1)]


if __name__ == '__main__':
    main()