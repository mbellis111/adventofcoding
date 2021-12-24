def main():
    # https://adventofcode.com/2021/day/10
    print("Starting...")

    with open("inputs/day_10_input_test.txt", 'r') as infile:
        lines = infile.readlines()

    matrix = parse_file(lines)
    print(matrix)

    # for part I
    # risk = calculate_risk_level(matrix)
    # print("Risk: {}".format(risk))

    print("Done!")


def parse_file(lines):
    rows = []
    for line in lines:
        row = [int(digit) for digit in line.strip()]
        rows.append(row)
    return rows


if __name__ == '__main__':
    main()
