
def main():
    # https://adventofcode.com/2021/day/3
    print("Starting...")

    with open("inputs/day_3_input.txt", 'r') as infile:
        lines = infile.readlines()

    # read_and_calculate(lines)
    matrix = read_to_matrix(lines)

    oxygen_rating_raw = calculate_oxygen_rating(matrix)
    print(oxygen_rating_raw)
    oxygen_rating = convert_list_to_int(oxygen_rating_raw)
    print(oxygen_rating)

    scrubber_rating_raw = calculate_scrubber_rating(matrix)
    print(scrubber_rating_raw)
    scrubber_rating = convert_list_to_int(scrubber_rating_raw)
    print(scrubber_rating)

    print("Product: {}".format(oxygen_rating * scrubber_rating))

    print("Done!")


def read_to_matrix(lines):
    matrix = []
    for line in lines:
        row = []
        for digit in line.strip():
            row.append(int(digit))
        matrix.append(row)
    return matrix


def get_most_common_by_column(matrix, column):
    num_ones = 0
    num_zeros = 0
    size = len(matrix[0])
    if column > size:
        return None

    for row in matrix:
        digit = row[column]
        if digit == 1:
            num_ones += 1
        elif digit == 0:
            num_zeros += 1

    if num_ones >= num_zeros:
        return 1
    return 0


def filter_keeping_matching(matrix, column, bit):
    filtered_matrix = []
    for row in matrix:
        if row[column] == bit:
            filtered_matrix.append(row)
    return filtered_matrix


def calculate_oxygen_rating(matrix):
    column = 0
    most_common_bit = get_most_common_by_column(matrix, column)
    remaining = filter_keeping_matching(matrix, column, most_common_bit)
    while len(remaining) > 1:
        column = column + 1
        most_common_bit = get_most_common_by_column(remaining, column)
        remaining = filter_keeping_matching(remaining, column, most_common_bit)
    return remaining[0]


def calculate_scrubber_rating(matrix):
    column = 0
    least_common_bit = flip(get_most_common_by_column(matrix, column))
    remaining = filter_keeping_matching(matrix, column, least_common_bit)
    while len(remaining) > 1:
        column = column + 1
        least_common_bit = flip(get_most_common_by_column(remaining, column))
        remaining = filter_keeping_matching(remaining, column, least_common_bit)
    return remaining[0]


def read_and_calculate(lines):
    size = len(lines)
    length = len(lines[0].strip())
    count_ones = [0] * length
    for line in lines:
        for i, digit in enumerate(line.strip()):
            if int(digit) == 1:
                count_ones[i] = count_ones[i] + 1
    # now find the most common bits
    common_bits = [0] * length
    for i, count in enumerate(count_ones):
        if count > size / 2:
            common_bits[i] = 1
        else:
            common_bits[i] = 0

    less_common_bits = [flip(bit) for bit in common_bits]

    print(common_bits)
    print(less_common_bits)

    gamma = convert_list_to_int(common_bits)
    epsilon = convert_list_to_int(less_common_bits)

    print(gamma)
    print(epsilon)

    power_consumption = gamma * epsilon
    print("Power Consumption: {}".format(power_consumption))


def flip(val):
    if val == 0:
        return 1
    elif val == 1:
        return 0
    return val

def convert_list_to_int(vals):
    strings = [str(val) for val in vals]
    binary_string = "".join(strings)
    int_val = int(binary_string, 2)
    return int_val

def read_data(lines):
    rows = []
    for line in lines:
        line = line.strip()
        row = []
        for digit in line:
            row.append(int(digit))
        rows.append(row)


if __name__ == '__main__':
    main()