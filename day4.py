
def main():
    # https://adventofcode.com/2021/day/4
    print("Starting...")

    with open("inputs/day_4_input.txt", 'r') as infile:
        lines = infile.readlines()

    numbers, boards = parse_file(lines)
    games = init_board(boards)
    print(numbers)
    print(games)

    # final_score = find_final_score(numbers, games)
    final_score = find_final_score_last(numbers, games)
    print(final_score)

    print("Done!")


def find_final_score(numbers, games):
    # ok, lets call numbers and check for wins
    for number in numbers:
        call_number(number, games)
        winner = check_games_for_win(games)
        if winner is not None:
            sum = sum_unmarked_numbers(winner)
            print(winner)
            print(sum)
            print(number)
            return sum * number
    return None


def find_final_score_last(numbers, games):
    # ok, lets call numbers and check for wins
    remaining = games
    for number in numbers:
        call_number(number, remaining)
        removed, remaining = remove_winning_boards(remaining)
        if not remaining:
            winner = removed[-1]
            sum = sum_unmarked_numbers(winner)
            print(winner)
            print(sum)
            print(number)
            return sum * number
    return None


def sum_unmarked_numbers(game):
    board = game["board"]
    marks = game["marks"]
    sum = 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            if marks[r][c] == 0:
                sum += board[r][c]
    return sum


def remove_winning_boards(games):
    removed = []
    remaining = []
    for game in games:
        if check_win(game["marks"]):
            removed.append(game)
        else:
            remaining.append(game)
    return removed, remaining


def check_games_for_win(games):
    for game in games:
        if check_win(game["marks"]):
            return game
    return None


def parse_file(lines):
    boards = []

    # the first line is the numbers to call
    first = lines[0]
    rest = lines[1:]

    numbers = first.strip().split(",")
    numbers = [int(digit) for digit in numbers]

    board = []
    for line in rest:
        line = line.strip()
        if not line:
            # if the board exists add it to the boards
            if board:
                boards.append(board)
            # make a new board
            board = []
            continue

        # starting parsing for the board
        line = line.split()
        line = [int(digit) for digit in line]
        board.append(line)
    if board:
        boards.append(board)

    return numbers, boards


def init_board(boards):
    games = []

    for board in boards:
        game = {}
        game["board"] = board
        game["marks"] = [[0] * len(board[0]) for i in range(len(board))]
        games.append(game)
    return games


def check_win(marks):
    # to win at bingo you need all of them in a row diag, horizontal, or vertical
    # so we need a bunch of loops, ew, python loops suck
    width = len(marks)
    height = len(marks[0])

    # check horizontal wins
    for row in range(width):
        if all(marks[row]):
            return True
    # check vertical wins
    for col in range(height):
        if all(get_column(marks, col)):
            return True

    return False


def get_column(marks, col):
    column = []
    width = len(marks)
    for row in range(width):
        column.append(marks[row][col])

    return column


def check_board_for_number(board, number):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == number:
                return r, c
    return None, None


def call_number(number, games):
    for game in games:
        r, c = check_board_for_number(game["board"], number)
        if r is not None and c is not None:
            game["marks"][r][c] = 1


if __name__ == '__main__':
    main()