def main():
    # https://adventofcode.com/2021/day/8
    print("Starting...")

    with open("inputs/day_8_input.txt", 'r') as infile:
        lines = infile.readlines()

    rows = parse_file(lines)

    total = 0
    for row in rows:
        input, output = row
        input_to_digit_map = create_input_to_digit_map(input)
        value = convert_output_to_value(output, input_to_digit_map)
        total += value
    print(total)

    # part I solution
    # num_unique_digits = get_num_unique_digits(rows)
    # print(num_unique_digits)

    print("Done!")


def create_input_to_digit_map(segments):
    # start with the easy ones
    one = filter_by_segment_count(segments, 2)[0]
    four = filter_by_segment_count(segments, 4)[0]
    seven = filter_by_segment_count(segments, 3)[0]
    eight = filter_by_segment_count(segments, 7)[0]
    three = find_three(segments, one)
    nine = find_nine(segments, four)
    zero = find_zero(segments, one, nine)
    six = find_six(segments, nine, zero)
    five = find_five(segments, three, six)
    two = find_two(segments, three, five)

    input_to_digit_map = {
        "".join(one): '1',
        "".join(two): '2',
        "".join(three): '3',
        "".join(four): '4',
        "".join(five): '5',
        "".join(six): '6',
        "".join(seven): '7',
        "".join(eight): '8',
        "".join(nine): '9',
        "".join(zero): '0'
    }
    return input_to_digit_map


# checks if the first segment contains all values in the second
def segment_contains(first, second):
    for val in second:
        if val not in first:
            return False
    return True


# the only 5 segment piece that contains all the one digits
def find_three(segments, one):
    filtered_segments = filter_by_segment_count(segments, 5)
    for segment in filtered_segments:
        if segment_contains(segment, one):
            return segment
    return None


# the only 6 segment piece that contains all of the four digits
def find_nine(segments, four):
    filtered_segments = filter_by_segment_count(segments, 6)
    for segment in filtered_segments:
        if segment_contains(segment, four):
            return segment
    return None


# the only six segment piece that contains one and isnt nine
def find_zero(segments, one, nine):
    filtered_segments = filter_by_segment_count(segments, 6)
    for segment in filtered_segments:
        # nine also contains one, so ignore it
        if segment == nine:
            continue
        # the only remaining segment that contains one
        if segment_contains(segment, one):
            return segment

    return None


# the only remaining six segment piece
def find_six(segments, nine, zero):
    filtered_segments = filter_by_segment_count(segments, 6)
    for segment in filtered_segments:
        # nine also contains one, so ignore it
        if segment == nine or segment == zero:
            continue
        return segment
    return None


# the only five digit segment that contains six has the digits of, that isnt three
def find_five(segments, three, six):
    filtered_segments = filter_by_segment_count(segments, 5)
    for segment in filtered_segments:
        if segment == three:
            continue
        # the six should contain everything in our segment
        if segment_contains(six, segment):
            return segment
    return None


# the only five digit segment that contains the digits in six and isnt three
def find_two(segments, three, five):
    filtered_segments = filter_by_segment_count(segments, 5)
    for segment in filtered_segments:
        if segment == three or segment == five:
            continue
        return segment
    return None


def parse_file(lines):
    rows = []
    for line in lines:
        values = line.strip().split(" | ")
        inputs = [sorted(value.strip()) for value in values[0].strip().split()]
        outputs = [sorted(value.strip()) for value in values[1].strip().split()]
        rows.append((inputs, outputs))
    return rows


def filter_by_segment_count(segments, number):
   return [segment for segment in segments if len(segment) == number]


def convert_output_to_value(output, input_to_digit_map):
    string_val = "{}{}{}{}".format(
        input_to_digit_map["".join(output[0])],
        input_to_digit_map["".join(output[1])],
        input_to_digit_map["".join(output[2])],
        input_to_digit_map["".join(output[3])]
    )
    val = int(string_val)
    return val


# for part I
def get_num_unique_digits(rows):
    count = 0
    for row in rows:
        # the outputs
        for segment in row[1]:
            if guess_digit_part_one(segment):
                count += 1
    return count


def guess_digit_part_one(segments):
    count = len(segments)
    if count == 2:
        return 1
    elif count == 4:
        return 4
    elif count == 3:
        return 7
    elif count == 7:
        return 8
    return None


if __name__ == '__main__':
    main()
