import time
import math


def main():
    # https://adventofcode.com/2021/day/16
    print("Starting...")

    start_time = time.perf_counter()

    with open("inputs/day_16_input.txt", 'r') as infile:
        lines = infile.readlines()

    # part I
    # required changes to parse packet, but very similar
    # just added the versions instead of the values

    # part II
    binary = parse_file(lines)
    pos, value = parse_packet(binary, 0)
    print(value)

    end_time = time.perf_counter()

    print("Executed code in {} seconds".format(end_time - start_time))
    print("Done!")


def parse_file(lines):
    # there should only be one line
    line = lines[0].strip()
    binary_string = []
    for val in line:
        binary_string.extend(hex_to_binary(val))
    return "".join(binary_string)


def hex_to_binary(hex_val):
    # convert to int from base 16 (hex)
    # then use format to convert to binary
    # left pad bytes less than 4 with a 0
    return format(int(hex_val, 16), '0>4b')


def parse_packet(binary, pos):
    # print("Packet")
    # first 3 bits are version
    version = int(binary[pos:pos+3], 2)
    pos += 3

    # next 3 bits are the packet type
    packet_type = int(binary[pos:pos+3], 2)
    pos += 3

    if packet_type == 4:
        pos, value = parse_literal(binary, pos)
        return pos, value

    # this an an operator packet
    # next bit handles the length type
    length_switch = binary[pos]
    pos += 1

    values = []
    if length_switch == '0':
        # the next 15 bits tells us the total bit length of subpackets to follow
        sub_length = int(binary[pos:pos + 15], 2)
        pos += 15

        packet_end = pos + sub_length
        while pos < packet_end:
            # get the data in the sub packet
            sub_packet = binary[pos:pos+sub_length]
            sub_pos, sub_val = parse_packet(sub_packet, 0)
            pos += sub_pos
            values.append(sub_val)
    elif length_switch == '1':
        # the next 11 bits are the number of subpackets to follow
        num_subpackets = int(binary[pos:pos + 11], 2)
        pos += 11
        for i in range(num_subpackets):
            pos, sub_val = parse_packet(binary, pos)
            values.append(sub_val)

    # now process the values based on the type
    value = None
    if packet_type == 0:
        value = sum(values)
    elif packet_type == 1:
        value = math.prod(values)
    elif packet_type == 2:
        value = min(values)
    elif packet_type == 3:
        value = max(values)
    elif packet_type == 5:
        value = 1 if values[0] > values[1] else 0
    elif packet_type == 6:
        value = 1 if values[0] < values[1] else 0
    elif packet_type == 7:
        value = 1 if values[0] == values[1] else 0

    return pos, value


def parse_literal(binary, pos):
    binary_value = ''
    # repeating amounts of 5 bits until the first bit is a 0
    seen_stop = False
    while not seen_stop:
        header = binary[pos]
        pos += 1
        if header == '0':
            seen_stop = True

        bits = binary[pos:pos+4]
        pos += 4
        binary_value += bits
    # discard remaining 0's at the end?
    int_value = int(binary_value, 2)
    return pos, int_value


if __name__ == '__main__':
    main()
