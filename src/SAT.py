import numpy as np

class SATSolver:

    def __init__(self, rules, puzzle, board_size = 9, multi=False):
        self.filename = puzzle
        #self.rules = self.read_dimacs(rules)
        self.board_size = board_size
        if not multi:
            self.puzzle = self.read_sudoku(puzzle)
        else:
            self.puzzles = self.read_multi_sudoku(puzzle)
    
    def read_multi_sudoku(self, filename):
        with open(filename, 'r') as input_file:
            data = input_file.read()
            puzzles = self.get_multi_puzzle(data)
        return puzzles

    def get_multi_puzzle(self, data):
        boards = []
        while data:
            board = np.zeros(shape=(self.board_size, self.board_size))
            for i in range(self.board_size):
                for j in range(self.board_size):
                    board[i][j] = data[0] if data and str.isnumeric(data[0]) else 0
                    data = data[1:]
            boards.append(board)
        return boards

    def read_sudoku(self, filename):
        with open(filename, 'r') as input_file:
            data = input_file.read()
            puzzle = self.get_puzzle(data)
        return puzzle
    
    def get_puzzle(self, data):
        board = np.zeros(shape=(self.board_size, self.board_size))
        for i in range(self.board_size):
            for j in range(self.board_size):
                board[i][j] = data[0] if str.isnumeric(data[0]) else 0
                data = data[1:]
        return board

                
        

x = SATSolver(None, 'sudoku/1000_sudokus.txt', board_size=9, multi=True)

for board in x.puzzles:
    print(board)