import sympy as sp
from Literal import Literal
from Model import Model
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
        self.model = Model
        self.clause_set = self.merge_sentences(self.ruleset, self.puzzle)

    def merge_sentences(self, ruleset, puzzle):
        clauses = [clause for clause in ruleset]
        for x in puzzle: clauses.append(x)
        return clauses

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
                    tokens = line.split()[:-1]
                    ls.append(self.get_symbols(tokens))
        return ls
    
    def get_symbols(self, tokens):
        return [self.get_literal(x) for x in tokens]
    
    def get_literal(self, token):
        negated = '-' in token
        symbol = token.strip('-')
        return Literal(negated, symbol)


    def simplify(self, S, p: Literal):
        S = [clause for clause in S if p not in clause]
        indexes = []
        for i in range(0, len(S)):
            for j in range(0, len(S[i])):
                if p and S[i][j] == -p:
                    indexes.append([i, j])
        for i, j in indexes:
            S[i].pop(j)
        return S

    # TODO
    # see https://www.cs.miami.edu/home/geoff/Courses/CSC648-12S/Content/DPLL.shtml
    def satisfiable(self, S):
        if len(S) == 0:
            return "SAT"
        while self.contains_unit_clause(S) or self.contains_pure_literal(S):
            p = self.next_unit_clause(S) 
            if p and p in S and -p in S:
                return "UNSAT"
'''

        S = []
S.append([Literal(), Literal(), Literal()])
S.append([Literal(), Literal(), Literal(True, 'x')])
S.append([Literal(), Literal(True, 'x'), Literal()])
S.append([Literal(), Literal(), Literal()])



'''
        

        

if __name__ == "__main__":
    x = SATSolver('dimacs/rulesets/9-rules.txt', 'dimacs/puzzles/sudoku.txt')
    print(x.ruleset)