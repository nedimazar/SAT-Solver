import sympy as sp
from Literal import Literal
class SATSolver:


    def __init__(self, ruleset_file, puzzle_file):
        """Reads in the ruleset and puzzle files.

        Args:
            ruleset_file (str): The path to the rules.
            puzzle_file (str): The path to the puzzle.
        """
        self.ruleset_file = ruleset_file
        self.puzzle_file = puzzle_file
        self.__set_rules_and_puzzle()

    def __set_rules_and_puzzle(self):
        """Reads the DIMACS files to get the rules and puzzle in memory.
        """
        self.ruleset = self.dimacs_to_list(self.ruleset_file)
        self.puzzle = self.dimacs_to_list(self.puzzle_file)

    def dimacs_to_list(self, dimacs_file):
        """Reads a DIMACS file and returns a representation so it can be stored in memory.

        Args:
            dimacs_file (str): Path to the DIMACS file.

        Returns:
            list: A list that represents the clauses inside the DIMACS file, a conjunction of clauses where each clause is a disjunction of literals.
        """
        ls = []
        with open(dimacs_file, 'r') as input_file:
            for line in input_file.readlines():
                if str.isnumeric(line[0]) or line[0] == '-':
                    tokens = line.split()
                    ls = self.get_symbols(tokens)
                    print(ls)
        return ls
    
    def get_symbols(self, tokens):
        return [self.get_literal(x) for x in tokens]
    
    def get_literal(self, token):
        negated = '-' in token
        symbol = token.strip('-')
        return Literal(negated, symbol)
    
    def solve(self):
        pass

x = SATSolver('dimacs/rulesets/9-rules.txt', 'dimacs/puzzles/sudoku.txt')
print(x.ruleset)