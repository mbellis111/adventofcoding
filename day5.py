
def main():
    # https://adventofcode.com/2021/day/4
    print("Starting...")

    with open("inputs/day_5_input_test.txt", 'r') as infile:
        lines = infile.readlines()

    line_segments = parse_file(lines)

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
        line_segments.append((first, second))

    # 6,4 -> 2,0

    return line_segments


def find_corners(line_segments):



if __name__ == '__main__':
    main()