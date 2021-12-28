import copy
import math


def show_board(entry):
    for i in range(len(entry)):
        row = entry[i]

        if i % 3 == 0 and i != 0:
            print("---------------------")

        print(row[0] + " " + row[1] + " " + row[2] + " | " +
              row[3] + " " + row[4] + " " + row[5] + " | " +
              row[6] + " " + row[7] + " " + row[8])


def set_board():
    preset_board = []
    for i in range(9):
        row = str(input("Enter row %d values (0 for blank): " % (i + 1)))
        preset_board.append(list(row))

    return preset_board


class Simple_Sudoku_Solver:

    def __init__(self, problem):
        self.board = problem
        self.all_number = list(str(x) for x in range(1, 10))
        self.solved = False

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
        iterations = 0

        while not self.solved:
            iterations += 1
            old_possibilities = copy.deepcopy(possibilities)

            for y in range(9):
                for x in range(9):
                    row_unique = set(self.all_number)
                    column_unique = set(self.all_number)
                    square_unique = set(self.all_number)

                    if len(possibilities[y][x]) != 1:
                        for k in range(9):
                            if x != k:
                                row_unique = row_unique - set(possibilities[y][k])
                            if y != k:
                                column_unique = column_unique - set(possibilities[k][x])
                        for i in range(3):
                            for j in range(3):
                                if x != math.floor(x / 3) * 3 + i or y != math.floor(y / 3) * 3 + j:
                                    square_unique = square_unique - set(
                                        possibilities[math.floor(y / 3) * 3 + j][math.floor(x / 3) * 3 + i])

                    if len(list(row_unique & set(possibilities[y][x]))) == 1:
                        possibilities[y][x] = list(row_unique & set(possibilities[y][x]))
                    elif len(list(column_unique & set(possibilities[y][x]))) == 1:
                        possibilities[y][x] = list(column_unique & set(possibilities[y][x]))
                    elif len(list(square_unique & set(possibilities[y][x]))) == 1:
                        possibilities[y][x] = list(square_unique & set(possibilities[y][x]))

            correct = True

            for y in range(9):
                for x in range(9):
                    if len(possibilities[y][x]) == 1:
                        possibilities[y][x] = possibilities[y][x][0]
                    else:
                        possibilities[y][x] = "0"
                        correct = False

            if not correct:
                new_possibilities = self.list_possibilities(possibilities)

                if old_possibilities != new_possibilities:
                    possibilities = new_possibilities
                else:
                    print("Sudoku is too complex for this method, unsolvable after %d iterations" % iterations)
                    return possibilities

            self.solved = correct

        print(str(iterations) + " iterations used")
        return possibilities

    def check_solution(self, solution):
        correct = True

        for y in range(9):
            if sorted(solution[y]) != self.all_number:
                correct = False

        for x in range(9):
            column = []
            for y in range(9):
                column.append(solution[y][x])

            if sorted(column) != self.all_number:
                correct = False

        for i in range(3):
            for j in range(3):
                square = []
                for m in range(3):
                    for n in range(3):
                        square.append(solution[i * 3 + m][j * 3 + n])

                if sorted(square) != self.all_number:
                    correct = False

        return correct


# board = [["0", "0", "0", "0", "6", "8", "0", "3", "0"],
#          ["1", "9", "0", "0", "0", "0", "0", "0", "0"],
#          ["8", "0", "3", "1", "0", "0", "2", "0", "0"],
#          ["4", "0", "0", "0", "5", "1", "0", "6", "0"],
#          ["7", "0", "0", "0", "2", "0", "0", "0", "4"],
#          ["0", "0", "0", "0", "7", "0", "8", "0", "0"],
#          ["0", "1", "0", "0", "0", "5", "0", "0", "7"],
#          ["0", "0", "4", "0", "0", "0", "0", "0", "0"],
#          ["0", "5", "0", "0", "3", "0", "1", "0", "0"]]

board = set_board()

print("Puzzle: ")
show_board(board)
print("")

solver = Simple_Sudoku_Solver(board)
my_answer = solver.simple_solve()

print("My answer:")
show_board(my_answer)

assert solver.check_solution(my_answer)
