# Python---Simple-Sudoku-Solver

This program aims to solve sudokus in a human way. 

It first lists all the possibilities of each block depending on the given values. Next it compares each block with other 
blocks in its row, column, and 3x3 square. If a block contains a unique value out of its row, column, and 3x3 square, 
said block will contain that value. After the program iterates through every block with undetermined values, all 
remaining undetermined blocks will be cleared. The board will be fed through the function that lists all possibilities 
for each block again, this time with the determined values from the previous iteration. 

This repeats until a solution is found, or if no additional values can be added to the board, which is when we know 
the sudoku is too complex for this method. Note, this algorithm does not aim to solve all sudokus. It simply solves 
those that can be solved by basic logical deductions. 