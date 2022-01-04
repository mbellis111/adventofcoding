import time
import math


def main():
    # https://adventofcode.com/2021/day/17
    print("Starting...")

    start_time = time.perf_counter()

    with open("inputs/day_17_input.txt", 'r') as infile:
        lines = infile.readlines()

    target_area = parse_file(lines)
    print(target_area)

    # part I
    # max_height = find_best_shot(target_area)
    # print("Max Height: ", max_height)

    # part II
    num_velocities = find_all_working_velocities(target_area)
    print("Working Velocities: ", num_velocities)

    end_time = time.perf_counter()

    print("Executed code in {} seconds".format(end_time - start_time))
    print("Done!")


def parse_file(lines):
    line = lines[0].strip()
    # target area: x=20..30, y=-10..-5
    line = line.replace("target area: ", "")
    left, right = line.split(", ")
    left = left.replace("x=", "")
    xmin, xmax = left.split("..")

    right = right.replace("y=", "")
    ymin, ymax = right.split("..")

    return int(xmin), int(xmax), int(ymin), int(ymax)


def find_best_shot(target_area):
    # start at 0, 0
    # continue until xv > xmax and yv > ymax or yv <= 0
    xmin, xmax, ymin, ymax = target_area
    any_hit = False
    best_height = float("-inf")
    # keep going until we overshoot the width in one step
    for xv in range(xmax + 1):
        # keep going until we overshoot the height in one step
        # because when y = 0 again, the velocity is -initial velocity
        for yv in range(-abs(ymin), abs(ymin)):
            max_height, hit_target = fire(xv, yv, target_area)
            if max_height and hit_target:
                # print("HIT! ({}, {}): {}".format(xv, yv, max_height))
                best_height = max(best_height, max_height)
                any_hit = True
    # we never hit
    if any_hit:
        return best_height
    return None


def find_all_working_velocities(target_area):
    # start at 0, 0
    # continue until xv > xmax and yv > ymax or yv <= 0
    xmin, xmax, ymin, ymax = target_area
    hit_velocities = set()
    # keep going until we overshoot the width in one step
    for xv in range(xmax + 1):
        # keep going until we overshoot the height in one step
        # because when y = 0 again, the velocity is -initial velocity
        for yv in range(-abs(ymin), abs(ymin)):
            max_height, hit_target = fire(xv, yv, target_area)
            if hit_target:
                # print("HIT! ({}, {}): {}".format(xv, yv, max_height))
                hit_velocities.add((xv, yv))
    # print(hit_velocities)
    return len(hit_velocities)


def fire(xv, yv, target_area):
    # start a 0, 0
    probe = [0, 0]
    max_height = float("-inf")
    hit_target = False

    while not past_target(probe[0], probe[1], xv, yv, target_area):
        # keep track of best height reached
        max_height = max(max_height, probe[1])

        # increase by xv and yv
        probe[0] += xv
        probe[1] += yv
        # decrease velocity
        xv = xv - 1 if xv > 0 else 0
        yv -= 1

        if in_target(probe[0], probe[1], target_area):
            hit_target = True

    # if we never hit return None for clarity later
    if not hit_target or max_height == float("-inf"):
        return None, False

    return max_height, hit_target


def in_target(x, y, target_area):
    xmin, xmax, ymin, ymax = target_area
    return xmin <= x <= xmax and ymin <= y <= ymax


def past_target(x, y, xv, yv, target_area):
    xmin, xmax, ymin, ymax = target_area
    if in_target(x, y, target_area):
        return False
    # xv decreases to 0
    if x > xmax and xv >= 0 or x < xmin and xv <= 0:
        return True
    # yv keeps decreasing
    if y < ymin and yv <= 0:
        return True
    return False


if __name__ == '__main__':
    main()
