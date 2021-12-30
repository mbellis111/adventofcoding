from collections import defaultdict, deque


def main():
    # https://adventofcode.com/2021/day/12
    print("Starting...")

    with open("inputs/day_12_input.txt", 'r') as infile:
        lines = infile.readlines()

    adj_map = parse_file(lines)
    print(adj_map)

    # for part I
    # total_paths = count_paths(adj_map)
    # print(total_paths)

    # for part II
    total_paths = count_paths(adj_map, True)
    print(total_paths)

    print("Done!")


def count_paths(adj_map, allow_extra_lower=False):
    total_paths = 0
    nodes = deque()
    nodes.append(("start", {"start"}, [], False))
    # keep trying until we run out of nodes
    while nodes:
        node, visited, path, extra_visit = nodes.popleft()

        # mark the node as visited
        visit_copy = set(visited)
        if node.islower():
            visit_copy.add(node)
        path_copy = path.copy()
        path_copy.append(node)

        if node == "end":
            # print(path_copy)
            total_paths += 1
            continue

        adj_nodes = adj_map[node]
        for adj_node in adj_nodes:
            if adj_node not in visited:
                nodes.append((adj_node, visit_copy, path_copy, extra_visit))
            elif allow_extra_lower and adj_node in visited and adj_node not in ["start", "end"] and not extra_visit:
                # if its been seen but its the first time we allowed one extra
                nodes.append((adj_node, visit_copy, path_copy, True))

    return total_paths


def parse_file(lines):
    adj_map = defaultdict(list)
    for line in lines:
        sn, en = line.strip().split("-")
        adj_map[sn].append(en)
        adj_map[en].append(sn)

    return adj_map


if __name__ == '__main__':
    main()
