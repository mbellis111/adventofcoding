def main():
    # https://adventofcode.com/2021/day/6
    print("Starting...")

    with open("inputs/day_6_input.txt", 'r') as infile:
        lines = infile.readlines()

    num_days = 256
    starting_fish = parse_file(lines)
    fish = create_fish_counter(starting_fish)
    print("Day 0: {}".format(fish))

    for day in range(num_days):
        fish = simulate_day(fish)
        print("Day {}: {}".format(day + 1, fish))

    total_fish = 0
    for days_left in fish:
        total_fish += fish[days_left]
    print("Total Fish: ", total_fish)

    print("Done!")


def create_fish_counter(starting_fish):
    fish = {
        0: len([fish for fish in starting_fish if fish == 0]),
        1: len([fish for fish in starting_fish if fish == 1]),
        2: len([fish for fish in starting_fish if fish == 2]),
        3: len([fish for fish in starting_fish if fish == 3]),
        4: len([fish for fish in starting_fish if fish == 4]),
        5: len([fish for fish in starting_fish if fish == 5]),
        6: len([fish for fish in starting_fish if fish == 6]),
        7: len([fish for fish in starting_fish if fish == 7]),
        8: len([fish for fish in starting_fish if fish == 8])
    }
    return fish


def simulate_day(fish):
    # move all fish down a day
    new_fish = {
        0: fish[1],
        1: fish[2],
        2: fish[3],
        3: fish[4],
        4: fish[5],
        5: fish[6],
        6: fish[7] + fish[0],
        7: fish[8],
        8: fish[0]
    }
    # for any fish that hit 0, create 8
    return new_fish


# def simulate_day(starting_fish):
#     new_fish = []
#     for i, fish in enumerate(starting_fish):
#         if fish == 0:
#             new_fish.append(8)
#             starting_fish[i] = 6
#         else:
#             starting_fish[i] = fish - 1
#     return starting_fish + new_fish

def parse_file(lines):
    line = lines[0]
    return [int(val) for val in line.split(",")]


if __name__ == '__main__':
    main()
