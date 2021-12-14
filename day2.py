
def main():
    # https://adventofcode.com/2021/day/2
    print("Starting...")

    with open("inputs/day_2_input.txt", 'r') as infile:
        lines = infile.readlines()

    calculate_positions(lines)

    calculate_positions_aim(lines)

    print("Done!")


def calculate_positions(lines):
    horizontal = 0
    depth = 0

    for line in lines:
        # formatted as
        # forward 5
        # down 5
        vals = line.strip().split()
        move = str(vals[0])
        amount = int(vals[1])

        if move == "forward":
            horizontal += amount
        elif move == "down":
            depth += amount
        elif move == "up":
            depth -= amount

    print("Horizontal: {}, Depth: {}, Mult: {}".format(horizontal, depth, horizontal * depth))

def calculate_positions_aim(lines):
    horizontal = 0
    depth = 0
    aim = 0

    for line in lines:
        # formatted as
        # forward 5
        # down 5
        vals = line.strip().split()
        move = str(vals[0])
        amount = int(vals[1])

        if move == "forward":
            horizontal += amount
            depth += aim * amount
        elif move == "down":
            aim += amount
        elif move == "up":
            aim -= amount

    print("Horizontal: {}, Depth: {}, Mult: {}".format(horizontal, depth, horizontal * depth))



if __name__ == '__main__':
    main()