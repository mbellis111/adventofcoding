

def main():
    print("Starting...")

    with open("inputs/day_1_input.txt", 'rb') as infile:
        lines = infile.readlines()

    count_num_increasing(lines)
    count_increasing_sliding(lines)


def count_increasing_sliding(lines):
    num_increasing = 0
    first = None
    second = None
    third = None
    curr_sum = None
    prev_sum = None

    for line in lines:
        first = int(line)
        if first and second and third:
            curr_sum = first + second + third
            if curr_sum and prev_sum:
                if curr_sum - prev_sum > 0:
                    num_increasing += 1
            prev_sum = curr_sum

        third = second
        second = first

    print(num_increasing)


def count_num_increasing(lines):
    num_increasing = 0

    prev = None
    curr = None
    for line in lines:
        curr = int(line)
        if prev and curr and curr - prev > 0:
            num_increasing += 1
        prev = curr
    print(num_increasing)

if __name__ == '__main__':
    main()
