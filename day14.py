
def main():
    # https://adventofcode.com/2021/day/14
    print("Starting...")

    with open("inputs/day_14_input.txt", 'r') as infile:
        lines = infile.readlines()

    data, mapping = parse_file(lines)
    print(data)
    print(mapping)

    # for part I
    # result = execute_steps(data, mapping, 10)
    # score = calc_score(result)
    # print("Score: {}".format(score))

    # for part II
    pair_count = create_pair_count(data)
    print(pair_count)
    execute_steps_paired(pair_count, mapping, 40)
    print(pair_count)
    score = calc_score_paired(pair_count)
    print("Score: {}".format(score))

    print("Done!")


def parse_file(lines):
    data = lines[0].strip()
    mapping = {}
    for line in lines[2:]:
        key, val = line.strip().split(" -> ")
        mapping[key] = val
    return data, mapping


def calc_score_paired(pair_count):
    # now calculate the score
    letter_count = {}
    for pair in pair_count:
        first = pair[0]
        num_pairs = pair_count[pair]
        add_to_pair_count(first, letter_count, num_pairs)
    print("Letter Count: ", letter_count)
    most_common = max(letter_count, key=letter_count.get)
    least_common = min(letter_count, key=letter_count.get)
    return letter_count[most_common] - letter_count[least_common]


def calc_score(data):
    count_dict = {}
    for c in data:
        if c not in count_dict:
            count_dict[c] = 1
        else:
            count_dict[c] = count_dict[c] + 1
    most_common = max(count_dict, key=count_dict.get)
    least_common = min(count_dict, key=count_dict.get)
    return count_dict[most_common] - count_dict[least_common]


def create_pair_count(data):
    # track how many pairs there are
    pair_count = {}
    length = len(data)
    first = 0
    second = 1
    while second < length:
        fc = data[first]
        sc = data[second]
        combined = fc + sc
        add_to_pair_count(combined, pair_count)
        first += 1
        second += 1
    # add the last letter in since it needs to be counted later
    pair_count[data[first]] = 1
    return pair_count


def execute_steps_paired(pair_count, mapping, steps):
    for _ in range(steps):
        execute_step_paired(pair_count, mapping)
    return pair_count


def execute_step_paired(pair_count, mapping):
    pair_copy = pair_count.copy()
    for pair in pair_copy:
        num_pairs = pair_copy[pair]
        # skip empty pairs
        if num_pairs == 0:
            continue
        if pair in mapping:
            # remove the current pairs
            add_to_pair_count(pair, pair_count, -1 * num_pairs)
            # add the two new pairs
            left = pair[0]
            right = pair[1]
            lp = left + mapping[pair]
            rp = mapping[pair] + right
            add_to_pair_count(lp, pair_count, num_pairs)
            add_to_pair_count(rp, pair_count, num_pairs)
    # pair_count = pair_copy


def add_to_pair_count(pair, mapping, count=1):
    if pair in mapping:
        mapping[pair] += count
    else:
        mapping[pair] = count


def execute_steps(data, map, num_steps):
    result = data
    for i in range(num_steps):
        result = execute_step(result, map)
    return result


def execute_step(data, mapping):
    new_data = []
    length = len(data)
    first = 0
    second = 1
    while second < length:
        fc = data[first]
        sc = data[second]
        combined = fc + sc
        if combined in mapping:
            new_data.append(fc)
            new_data.append(mapping[combined])
        else:
            new_data.append(fc)
        first += 1
        second += 1
    new_data.append(data[first])
    return "".join(new_data)


if __name__ == '__main__':
    main()
