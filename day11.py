def main():
    # https://adventofcode.com/2021/day/11
    print("Starting...")

    with open("inputs/day_11_input.txt", 'r') as infile:
        lines = infile.readlines()

    matrix = parse_file(lines)

    # for part I
    # total_flash_count = simulate_days(matrix, 100)
    # print("Total Flash Count: {}".format(total_flash_count))

    # for part II
    day = find_first_all_flash(matrix, 1000)
    print("First All Flash: {}".format(day))

    print("Done!")


def simulate_days(matrix, days):
    total_flash_count = 0
    for _ in range(days):
        flash_count = simulate_day(matrix)
        total_flash_count += flash_count
    return total_flash_count


def find_first_all_flash(matrix, days):
    total_cells = len(matrix) * len(matrix[0])
    for day in range(days):
        flash_count = simulate_day(matrix)
        if flash_count == total_cells:
            # zero based
            return day + 1
    return None


def simulate_day(matrix):
    width = len(matrix)
    height = len(matrix[0])
    flashes = [[0] * width for _ in range(height)]
    # print(flashes)

    # increase each value by 1
    for r in range(width):
        for c in range(height):
            matrix[r][c] = matrix[r][c] + 1

    # anything greater than 9 flashes
    for r in range(width):
        for c in range(height):
            value = matrix[r][c]
            if value > 9:
                flash(matrix, r, c, flashes)

    # each flash gets reset to 0
    flash_count = 0
    for r in range(width):
        for c in range(height):
            if flashes[r][c] == 1:
                matrix[r][c] = 0
                flash_count += 1

    return flash_count


def flash(matrix, r, c, flashes):
    # any position can only flash once
    if flashes[r][c] == 1:
        return
    # mark position as flashed
    flashes[r][c] = 1
    # a flash increases all adj positions by 1
    adj_list = get_adj(matrix, r, c)
    # increase the values now for adj positions
    for position in adj_list:
        pr, pc = position
        matrix[pr][pc] += 1
        if matrix[pr][pc] > 9 and flashes[pr][pc] != 1:
            flash(matrix, pr, pc, flashes)


def get_adj(matrix, r, c):
    width = len(matrix)
    height = len(matrix[0])
    adj_list = []
    for position in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
        nr = r + position[0]
        nc = c + position[1]
        if nr < width and nr >= 0 and nc < height and nc >= 0:
            adj_list.append((nr, nc))
    return adj_list


def parse_file(lines):
    rows = []
    for line in lines:
        row = [int(token) for token in line.strip()]
        rows.append(row)
    return rows


if __name__ == '__main__':
    main()
