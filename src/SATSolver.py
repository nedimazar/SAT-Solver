import numpy as np

class SATSolver:

    def __init__(self, ruleset_file, puzzle_file, board_size = 9):
        self.ruleset_file = ruleset_file
        self.puzzle_file = puzzle_file
        self.board_size = board_size
        self.set_rules_and_puzzle()

    def set_rules_and_puzzle(self):
        self.ruleset = self.dimacs_to_list(self.ruleset_file)
        self.puzzle = self.dimacs_to_list(self.puzzle_file)

    def dimacs_to_list(self, dimacs_file):
        ls = []
        with open(dimacs_file, 'r') as input_file:
            for line in input_file.readlines():
                if str.isnumeric(line[0]) or line[0] == '-':
                    tokens = line.split()
                    ls.append(tokens[:-1])
        return ls
    
    def solve(self):
        pass

x = SATSolver('dimacs/rulesets/9-rules.txt', 'dimacs/puzzles/sudoku.txt')

print(x.puzzle)