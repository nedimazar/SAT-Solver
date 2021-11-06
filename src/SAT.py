import numpy as np

class SATSolver:

    def __init__(self, rules, puzzle_file, board_size = 9):
        self.rules = rules
        self.puzzle_file = puzzle_file
        self.board_size = board_size
        self.puzzles = self.read_sudoku(self.puzzle_file)

    
    def write_dimacs(self, puzzle=None):
        if not puzzle:
            puzzle = self.puzzles[0]
        name = self.puzzle_file.split("/")[1]
        with open(f'out/{name}.out', 'w') as out:
            for i, row in enumerate(puzzle):
                for j, pos in enumerate(row):
                    if pos > 0:
                        out.write(f"{i+1}{j+1}{int(pos)} 0\n")

    def read_sudoku(self, filename):
        boards = []
        with open(filename, 'r') as input_file:
            lines = input_file.readlines()
            for line in lines:
                board = np.zeros(shape=(self.board_size, self.board_size))
                x = 0
                for i in range(self.board_size):
                    for j in range(self.board_size):
                        board[i][j] = line[x] if str.isnumeric(line[x]) else 0
                        x+=1
                boards.append(board)
        return boards

x = SATSolver(None, 'sudoku/1000_sudokus.txt', board_size=9)
#x.
x.write_dimacs()
