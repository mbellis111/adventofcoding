import time
from heapq import *


def main():
    # https://adventofcode.com/2021/day/15
    print("Starting...")

    start_time = time.perf_counter()

    with open("inputs/day_15_input.txt", 'r') as infile:
        lines = infile.readlines()

    matrix = parse_file(lines)
    # for row in matrix:
    #     print(row)

    # part I
    # start = (0, 0)
    # end = (len(matrix) - 1, len(matrix[0]) - 1)
    # cost = a_star(matrix, start, end, False)
    # print("Cost: ", cost)

    # part II
    bigger_matrix = biggify_matrix(matrix)
    start = (0, 0)
    end = (len(bigger_matrix) - 1, len(bigger_matrix[0]) - 1)
    cost = a_star(bigger_matrix, start, end, False)
    print("Cost: ", cost)

    end_time = time.perf_counter()

    print("Executed code in {} seconds".format(end_time - start_time))
    print("Done!")


def parse_file(lines):
    matrix = []
    for line in lines:
        vals = line.strip()
        row = [int(val) for val in vals]
        matrix.append(row)
    return matrix


def biggify_matrix(matrix):
    # the matrix is five times larger in both directions
    # matrix = [[0] * (width + 1) for _ in range(height + 1)]
    orig_width = len(matrix)
    orig_height = len(matrix[0])
    big_matrix = [[0] * orig_width * 5 for _ in range(orig_height * 5)]

    for r in range(len(big_matrix)):
        for c in range(len(big_matrix[r])):
            if r < orig_width and c < orig_height:
                big_matrix[r][c] = matrix[r][c]
                continue
            # look the previous value from the left, if you can't, then look up
            if r >= orig_width:
                pr = r - orig_width
                pc = c
            else:
                pr = r
                pc = c - orig_height
            # print(r, ",", c)
            prev_value = big_matrix[pr][pc]
            if prev_value == 9:
                prev_value = 0
            # the new value is difference between the original
            big_matrix[r][c] = prev_value + 1

    return big_matrix


# based on https://en.wikipedia.org/wiki/A*_search_algorithm
def a_star(matrix, start, end, allow_diag=False):
    # nodes to visit
    open_set = []
    # cheapest path from start to node currently known
    g_score = {}
    # cheapest path from start to node + guess to end
    f_score = {}

    # add the start
    heappush(open_set, (0, start))
    g_score[start] = 0
    f_score[start] = heuristic_cost(start, end, allow_diag)

    while open_set:
        current_node = heappop(open_set)
        current = current_node[1]

        # if we've reached the end goal, return the actual cost to the node
        if current == end:
            return g_score[current]

        neighbors = get_neighbors(matrix, current[0], current[1], allow_diag)
        for neighbor in neighbors:
            tentative_gscore = g_score[current] + matrix[neighbor[0]][neighbor[1]]
            if neighbor not in g_score or tentative_gscore < g_score[neighbor]:
                g_score[neighbor] = tentative_gscore
                f_score[neighbor] = tentative_gscore + heuristic_cost(neighbor, end, allow_diag)
                if neighbor not in open_set:
                    heappush(open_set, (f_score[neighbor], neighbor))
    # no path found
    return None


# this calculates the cost of moving from the current node to the end
def heuristic_cost(start, end, allow_diag):
    norm_cost = 1
    diag_cost = 1
    dx = abs(start[0] - end[0])
    dy = abs(start[1] - end[1])

    # if its not diagonal, just use manhattan cost
    if not allow_diag:
        return norm_cost * (dx + dy)
    # otherwise use euclidian distance
    return norm_cost * max(dx, dy) + (diag_cost - norm_cost) * min(dx, dy)


def get_neighbors(matrix, r, c, allow_diag):
    end_r = len(matrix)
    end_c = len(matrix[0])
    neighbors = []
    if allow_diag:
        vals = [(1, 1), (1, 0), (1, -1), (-1, 0), (-1, -1), (-1, 1), (0, 1), (0, -1)]
    else:
        vals = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for rc, cc in vals:
        nr = r + rc
        nc = c + cc
        if nr >= 0 and nr < end_r and nc >= 0 and nc < end_c:
            neighbors.append((nr, nc))

    return neighbors


if __name__ == '__main__':
    main()
