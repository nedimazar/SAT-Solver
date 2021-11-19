from typing import List
from Literal import Literal
from Model import Model

class Formula:

    def __init__(self, clauses) -> None:
        self.formula = clauses
        self.unit_clauses = list(self.get_unit_clauses())
        self.model = Model(self.formula)
    
    def get_unit_clauses(self) -> List:
        for clause in self.formula:
            if len(clause) == 1:
                yield clause

    '''
    A partial assignment for a formula F is a truth assignment to a subset of the variables of F. For a partial assignment ρ for a CNF formula F, F|ρ denotes the simplified formula obtained by replacing the variables appearing in ρ with their specified values, removing all clauses with at least one TRUE literal, and deleting all occurrences of FALSE literals from the remaining clauses.
    '''
    def simplify(self, formula, literal):
        for i, clause in enumerate(formula):
            for j, variable in enumerate(clause):
                if variable.abs() in literal.keys():
                    polarity = literal[variable.abs()]
                    if variable.negated:
                        formula[i][j] = str(not polarity)
                    else:
                        formula[i][j] = str(polarity)

        for i, clause in enumerate(formula):
            if 'True' in clause:
                formula.pop(i)

        for i, clause in enumerate(formula):
            for j, literal in enumerate(clause):
                if literal == 'False':
                    formula[i].pop(j)
        return formula
            
    
    def unit_propagate(self, F, p):
        while [] not in F and len(self.unit_clauses) > 0:
            x = self.unit_clauses.pop()[0]
            if x.negated:
                F = self.simplify(F, {x.abs() : False})
            else:
                F = self.simplify(F, {x.abs() : True})
            p = p.union(x)
        return F, p
    
    def DPLL(self):
        return self.DPLL_recursive(self.formula, self.model)
    
    def DPLL_recursive(self, F, p):
        (F, p) = self.unit_propagate(F, p)
        if [] in F:
            return 'UNSAT'
        if F == []:
            print(p)
            return 'SAT'

        l = p.next_unassigned()

        if self.DPLL_recursive(
            F = self.simplify(F, {l : True}),
            p = p.union(l),
        ) == 'SAT': return 'SAT'

        return self.DPLL_recursive(
            F = self.simplify(F, {l : False}),
            p = p.union(-l)
        )
