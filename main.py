import math


class Board:

    def __init__(self):
        self.board = [["0", "0", "0", "0", "0", "0", "0", "8", "0"],
                      ["6", "8", "0", "4", "7", "0", "0", "2", "0"],
                      ["0", "1", "9", "5", "0", "8", "6", "4", "7"],
                      ["0", "6", "0", "9", "0", "0", "0", "0", "4"],
                      ["3", "4", "2", "6", "8", "0", "0", "0", "0"],
                      ["1", "9", "0", "0", "5", "0", "8", "3", "0"],
                      ["0", "0", "0", "7", "2", "0", "4", "0", "3"],
                      ["0", "0", "6", "0", "0", "5", "0", "1", "0"],
                      ["0", "0", "3", "8", "9", "1", "5", "0", "0"]]

        self.answer = [["6", "4", "9", "5", "2", "7", "1", "3", "8"],
                       ["5", "3", "1", "8", "9", "4", "2", "7", "6"],
                       ["8", "2", "7", "1", "6", "3", "9", "4", "5"],
                       ["4", "9", "6", "3", "8", "2", "7", "5", "1"],
                       ["2", "1", "8", "4", "7", "5", "6", "9", "3"],
                       ["7", "5", "3", "9", "1", "6", "4", "8", "2"],
                       ["9", "6", "2", "7", "3", "8", "5", "1", "4"],
                       ["3", "7", "4", "6", "5", "1", "8", "2", "9"],
                       ["1", "8", "5", "2", "4", "9", "3", "6", "7"]]


def show_board(board):
    for i in range(len(board)):
        row = board[i]

        if i % 3 == 0 and i != 0:
            print("---------------------")

        print(row[0] + " " + row[1] + " " + row[2] + " | " +
              row[3] + " " + row[4] + " " + row[5] + " | " +
              row[6] + " " + row[7] + " " + row[8])


class Simple_Sudoku_Solver:

    def __init__(self, problem):
        self.board = problem
        self.all_number = list(str(x) for x in range(1, 10))
        self.solved = False

    def naive_solve(self):
        # while not self.solved:
        for k in range(1):
            for y in range(9):
                for x in range(9):
                    if self.board[y][x] == "0":
                        row = self.board[y]
                        column = []
                        for i in self.board:
                            column.append(i[x])
                        square = []
                        for i in range(0, 3):
                            for j in range(0, 3):
                                square.append(self.board[math.floor(y / 3) + i][math.floor(x / 3) + j])

                        if len(list(set(self.all_number) - set(row))) == 1:
                            self.board[y][x] = (set(self.all_number) - set(row))[0]
                        elif len(list(set(self.all_number) - set(column))) == 1:
                            self.board[y][x] = (set(self.all_number) - set(row))[0]
                        elif len(list(set(self.all_number) - set(square))) == 1:
                            self.board[y][x] = (set(self.all_number) - set(row))[0]

                    print(x, y, self.board[y][x])

            for row in self.board:
                if "0" in row:
                    break
                self.solved = True

    def list_possibilities(self, in_board):
        board_possibilities = []

        for y in range(9):
            board_possibilities.append([])

            for x in range(9):
                board_possibilities[y].append([])

                if in_board[y][x] == "0":
                    row = in_board[y]
                    column = []
                    for i in in_board:
                        column.append(i[x])
                    square = []
                    for i in range(0, 3):
                        for j in range(0, 3):
                            square.append(in_board[math.floor(y / 3) * 3 + i][math.floor(x / 3) * 3 + j])

                    row_allowed = set(self.all_number) - set(row)
                    column_allowed = set(self.all_number) - set(column)
                    square_allowed = set(self.all_number) - set(square)

                    board_possibilities[y][x] = list(row_allowed & column_allowed & square_allowed)
                else:
                    board_possibilities[y][x] = list(in_board[y][x])

        return board_possibilities

    def simple_solve(self):
        possibilities = self.list_possibilities(self.board)

        while not self.solved:
            for y in range(9):
                for x in range(9):
                    unique = set(self.all_number)
                    if len(possibilities[y][x]) != 1:
                        for k in range(9):
                            if x != k:
                                unique = unique - set(possibilities[y][k])
                            if y != k:
                                unique = unique - set(possibilities[k][x])
                        for i in range(3):
                            for j in range(3):
                                if x != math.floor(x / 3) * 3 + i or y != math.floor(y / 3) * 3 + j:
                                    unique = unique - set(possibilities[math.floor(y / 3) * 3 + j][math.floor(x / 3) * 3 + i])

                    if len(list(unique & set(possibilities[y][x]))) == 1:
                        possibilities[y][x] = list(unique & set(possibilities[y][x]))

            correct = True

            for y in range(9):
                for x in range(9):
                    if len(possibilities[y][x]) == 1:
                        possibilities[y][x] = possibilities[y][x][0]
                    else:
                        possibilities[y][x] = "0"
                        correct = False

            if not correct:
                possibilities = self.list_possibilities(possibilities)

            self.solved = correct

        return possibilities


board = Board()

print("Puzzle: ")

show_board(board.board)

print("Solving...")

solver = Simple_Sudoku_Solver(board.board)
my_answer = solver.simple_solve()

print("My answer:")
show_board(my_answer)
print("Official answer:")
show_board(board.answer)

if my_answer == board.answer:
    print("SAME")
else:
    print("Incorrect")


