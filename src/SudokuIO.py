import numpy as np
class SudokuIO:
    def __init__(self, puzzle_file, board_size = 9):
        self.puzzle_file = puzzle_file
        self.board_size = board_size
        self.puzzles = self.read_sudoku(puzzle_file)

    def write_dimacs(self, puzzle=None):
        if puzzle is None:
            puzzle = self.puzzles[0]
        name = self.puzzle_file.split("/")[1]
        with open(f'dimacs/puzzles/{name}7', 'w') as out:
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

def main():
    io = SudokuIO('sudoku/1000_sudokus.txt')
    io.write_dimacs(io.puzzles[7])

if __name__ == '__main__':
    main()