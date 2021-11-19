from typing import List
from Literal import Literal
from Model import Model
import copy

class Formula:

    def __init__(self, clauses) -> None:
        self.formula = clauses
        self.unit_clauses = list(self.get_unit_clauses())
        
        self.model = Model(self.formula)
    
    def get_unit_clauses(self) -> List:
        for clause in [self.formula]:
            if len(clause) == 1:
                yield clause

    '''
    A partial assignment for a formula F is a truth assignment to a subset of the variables of F. For a partial assignment ρ for a CNF formula F, F|ρ denotes the simplified formula obtained by replacing the variables appearing in ρ with their specified values, removing all clauses with at least one TRUE literal, and deleting all occurrences of FALSE literals from the remaining clauses.
    '''
    def simplify(self, formula, literal):
        newF = []
        for i, clause in enumerate(formula):
            newClause = []
            for j, variable in enumerate(clause):
                if variable.abs() in literal.keys():
                    polarity = literal[variable.abs()]
                    if variable.negated:
                        d = str(not polarity)
                    else:
                        d = str(polarity)
                    if d != 'False':
                        newClause.append(d)
                else:
                    newClause.append(variable)
            if 'True' not in newClause:
                newF.append(newClause)

        # The number of clauses goes below 1697 but then it backtracks and gets
        # stuck
        print("Number of clauses in formula:", len(newF))

        return newF
    
    def flatten(self, nested):
            return [item for sublist in nested for item in sublist]
            
    
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

        #TODO This assignment gets towards the end (We run out of variables
        # to set, however the solution is not comlete)
        l = p.next_unassigned()

        if self.DPLL_recursive(
            F = self.simplify(F, {l : True}),
            p = p.union(l),
        ) == 'SAT': return 'SAT'

        return self.DPLL_recursive(
            F = self.simplify(F, {l : False}),
            p = p.union(-l)
        )
