import math 


class Board:

    def __init__(self):
        self.board = [["0", "4", "0", "0", "0", "7", "1", "0", "0"],
                      ["5", "3", "0", "0", "9", "0", "0", "7", "0"],
                      ["0", "0", "7", "0", "6", "0", "9", "4", "0"],
                      ["4", "0", "6", "0", "8", "0", "7", "5", "1"],
                      ["0", "1", "0", "0", "0", "0", "6", "9", "0"],
                      ["0", "5", "3", "0", "1", "0", "0", "0", "2"],
                      ["9", "6", "0", "0", "3", "0", "0", "1", "0"],
                      ["3", "7", "0", "0", "5", "1", "0", "0", "0"],
                      ["1", "0", "0", "2", "0", "9", "3", "6", "7"]]
    
    def show_board(self):
        for i in range(len(self.board)):
            row = self.board[i]

            if i % 3 == 0 and i != 0:
                print("---------------------")

            print(row[0] + " " + row[1] + " " + row[2] + " | " + 
                  row[3] + " " + row[4] + " " + row[5] + " | " + 
                  row[6] + " " + row[7] + " " + row[8])

    def preset_values(self, entries):
        # entry is an array with entries: [i, j, k]
        # where i and j are the (x, y) coordinates and k is the value

        for entry in entries:
            i = entry[0]
            j = entry[1]
            k = entry[2]

            self.board[j][i] = k


class Simple_Sudoku_Solver():

    def __init__(self, board):
        self.board = board
        self.all_number = []
        self.solved = False
    
    def naive_solve(self):
        for i in range(1, 10):
            self.all_number.append(str(i))

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


                



board = Board()

board.show_board()

solver = Simple_Sudoku_Solver(board.board)

board.show_board()



