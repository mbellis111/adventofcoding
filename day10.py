def main():
    # https://adventofcode.com/2021/day/10
    print("Starting...")

    with open("inputs/day_10_input.txt", 'r') as infile:
        lines = infile.readlines()

    rows = parse_file(lines)

    # for part I
    # total_score = get_total_corrupted_score(rows)
    # print("Total Score: {}".format(total_score))

    # for part II
    scores = []
    for row in rows:
        score = score_incomplete_line(row)
        if score:
            scores.append(score)
    scores = sorted(scores)
    # take the middle score
    print(scores)
    print(len(scores))
    winner_pos = int(len(scores) / 2)
    print("Winner Score: {}".format(scores[winner_pos]))

    print("Done!")


def parse_file(lines):
    rows = []
    for line in lines:
        row = [token for token in line.strip()]
        rows.append(row)
    return rows


def get_total_corrupted_score(rows):
    total_score = 0
    for row in rows:
        score = score_corrupted_line(row)
        if score:
            total_score += score_corrupted_line(row)
    return total_score


def score_incomplete_line(line):
    token_stack = []
    for token in line:
        if is_left(token):
            token_stack.append(token)
        else:
            # pop the item and ensure it matches
            left_token = token_stack.pop()
            compliment = get_complimentary(left_token)
            if compliment != token:
                # this is corrupted and should be skipped
                return 0
    # whatever tokens are left in the stack need to be considered
    score = 0
    while token_stack:
        token = token_stack.pop()
        score *= 5
        score += calc_score_incomplete(get_complimentary(token))
    return score


def score_corrupted_line(line):
    token_stack = []
    for token in line:
        if is_left(token):
            token_stack.append(token)
        else:
            # pop the item and ensure it matches
            left_token = token_stack.pop()
            compliment = get_complimentary(left_token)
            if compliment != token:
                print("Expected {} but got {}".format(compliment, token))
                return calc_score(token)
    return 0


def get_complimentary(token):
    if token == '(':
        return ')'
    elif token == '[':
        return ']'
    elif token == '{':
        return '}'
    elif token == '<':
        return '>'
    return None


def is_left(token):
    return token in ['(', '[', '{', '<']


def calc_score_incomplete(token):
    if token == ')':
        return 1
    elif token == ']':
        return 2
    elif token == '}':
        return 3
    elif token == '>':
        return 4
    return None


def calc_score(token):
    if token == ')':
        return 3
    elif token == "]":
        return 57
    elif token == "}":
        return 1197
    elif token == ">":
        return 25137
    return None


if __name__ == '__main__':
    main()
