def main():
    # https://adventofcode.com/2021/day/7
    print("Starting...")

    with open("inputs/day_7_input.txt", 'r') as infile:
        lines = infile.readlines()

    values = parse_file(lines)

    fuel_cost = find_cheapest_total_cost(values)
    print(fuel_cost)

    print("Done!")


def parse_file(lines):
    line = lines[0]
    return [int(val) for val in line.split(",")]


def find_cheapest_total_cost(values):
    cheapest_fuel_cost = None
    for value in values:
        fuel_cost = align_on_value(values, value)
        if not cheapest_fuel_cost:
            cheapest_fuel_cost = fuel_cost
        cheapest_fuel_cost = min(fuel_cost, cheapest_fuel_cost)
    return cheapest_fuel_cost


# used to memoize the cost function
fuel_cache = [0, 1]


def calculate_fuel_cost(start, end):
    num_steps = abs(start - end)
    # part I
    # return num_steps

    # part II
    if num_steps < len(fuel_cache):
        return fuel_cache[num_steps]

    # otherwise populate until we hit the position
    pos = len(fuel_cache) - 1
    while pos < num_steps:
        fuel_cost = fuel_cache[pos]
        fuel_cache.append(fuel_cost + pos + 1)
        pos += 1
    return fuel_cache[num_steps]


def align_on_value(values, align_value):
    fuel_cost = 0

    for value in values:
        cost = calculate_fuel_cost(value, align_value)
        fuel_cost += cost

    return fuel_cost


if __name__ == '__main__':
    main()
