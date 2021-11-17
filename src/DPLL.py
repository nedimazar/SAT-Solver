import math
import random
from SATSolver import *
from collections import defaultdict
import operator

def get_counter(formula):
    counter = {}
    for clause in formula.clauses:
        for literal in clause:
            if literal in counter:
                counter[literal] += 1
            else:
                counter[literal] = 1
    return counter



def get_pure_literals(formula):
    counter = get_counter(formula)
    #print("coun", counter)
    pures = []
    for literal, times in counter.items():
        if -literal not in counter:
            pures.append(literal)
    #print("pures", pures)
    return pures

def get_unit_clauses(formula):
    unit_clauses = [c for c in formula.clauses if len(c) == 1]
    flat_list = []
    for sublist in unit_clauses:
        for item in sublist:
            flat_list.append(item)
    return flat_list

def get_next_unit_clause(formula):
    unit_clauses = get_unit_clauses(formula)
    for i in range(0,len(unit_clauses)):
        return unit_clauses.pop(i)

def get_next_pure_literal(formula):
    pures = get_pure_literals(formula)
    for i in range(0,len(pures)):
        return pures.pop(i)

def contains_unit_clauses(formula):
    unit_clauses = get_unit_clauses(formula)
    return len(unit_clauses) > 0

def contains_pure_literal(formula):
    pures = get_pure_literals(formula)
    return len(pures) > 0

def next_p(formula):
    if contains_unit_clauses(formula):
        return get_next_unit_clause(formula)
    if contains_pure_literal(formula):
        return get_next_pure_literal(formula)

def simplify(formula, p):
    # Delete every clause in S containing p
    formula.clauses = [clause for clause in formula.clauses if p not in clause]
    #print("cl",clauses)
    # Delete every occurence in S of -p
   # formula = clauses
    #print("formula",formula)

    indexes = []
    for i in range(0, len(formula)):
        for j in range(0, len(formula.clauses[i])):
            #print("oo2",-p,formula.clauses[i][j])
            if p and formula.clauses[i][j] == -p:
                indexes.append([i, j])
                #print("HERE")
    for i, j in indexes:
        formula.clauses[i].pop(j)
    return formula

def get_longest(clauses):
    save = []
    longest = 0
    shortest_index = {}
    for i, clause in enumerate(clauses):
        save.append([])
        if len(clause) in shortest_index:
            shortest_index[len(clause)].append(clause)
        else:
            shortest_index[len(clause)] = [clause]
        if len(clause) > longest:
            longest = len(clause)
    return longest, shortest_index

def from_shortest_clause(formula):
    #clauses = [clause for clause in formula]
    longest, shortest_index = get_longest(formula.clauses)
    for x in range(longest + 1):
        if x in shortest_index:
            p = shortest_index[x].pop()
            if len(shortest_index[x]) == 0:
                shortest_index.pop(x)
            return p
    return None

def satisfiable(formula):
    if len(formula) == 0:
        return "SAT"
    while contains_unit_clauses(formula) or contains_pure_literal(formula):
        p = next_p(formula)
        if (p in formula.clauses) and (-p in formula.clauses):
            return "UNSAT"
        else:
            formula = simplify(formula, p)
    if len(formula) == 0:
        return "SAT"
    p = from_shortest_clause(formula)
    if (satisfiable(simplify(formula, p)) == "SAT"):
        return "SAT"
    else:
        return (satisfiable(simplify(formula, -p)))

def satisfiable_DLCS(formula):
    if len(formula) == 0:
        return "SAT"
    while contains_unit_clauses(formula) or contains_pure_literal(formula):
        p = next_p(formula)
        if (p in formula.clauses) and (-p in formula.clauses):
            return "UNSAT"
        else:
            formula = simplify(formula, p)
    if len(formula) == 0:
        return "SAT"
    (p, CP_bigger_than_CN) = get_largest_CPCN(formula)
    
    if CP_bigger_than_CN:
        if (satisfiable_DLCS(simplify(formula, p)) == "SAT"):
            return "SAT"
        else:
            return (satisfiable_DLCS(simplify(formula, -p)))
    else:
        if (satisfiable_DLCS(simplify(formula, -p)) == "SAT"):
            return "SAT"
        else:
            return (satisfiable_DLCS(simplify(formula, p)))

def satisfiable_mom(formula):
    if len(formula) == 0:
        return "SAT"
    while contains_unit_clauses(formula) or contains_pure_literal(formula):
        p = next_p(formula)
        if (p in formula.clauses) and (-p in formula.clauses):
            return "UNSAT"
        else:
            formula = simplify(formula, p)
    if len(formula) == 0:
        return "SAT"
    p = moms(formula)
    if (satisfiable(simplify(formula, p)) == "SAT"):
        return "SAT"
    else:
        return (satisfiable(simplify(formula, -p)))

def get_total_count(item, sentences):
    return sum([sentence.count(item) for sentence in sentences])

def get_largest_CPCN(formula):
    counts = {}
    m = [None, -1, -1]
    for x in formula:
        for y in x:
            if y.abs() in counts:
                continue
            else:
                counts[y.abs()] = {'CP': get_total_count(Literal(False, y.symbol)),
                                    'CN' : get_total_count(Literal(True, y.symbol))}
                CP = counts[y.abs()]['CP']
                CN = counts[y.abs()]['CN']

                if CP + CN > m[1] + m[2]:
                    m = [y.abs(), CP, CN]
    return (m[0], m[1] > m[2])

def get_clause_size(clause):
    counter = 0
    for literal in clause:
        counter = counter + 1
    return counter

def get_most_occurent_literal(formula):
    counter = get_counter(formula)
    return max(counter.items(), key=operator.itemgetter(1))[0]

def minClauses(clauses):
    minClauses = [];
    size = -1;
    for clause in clauses:
        clauseSize = get_clause_size(clause)
        # Either the current clause is smaller
        if size == -1 or clauseSize < size:
            minClauses = [clause]
            size = clauseSize
        # Or it is of minimum size as well
        elif clauseSize == size:
            minClauses.append(clause)
    return minClauses

def moms(formula):
    minc = minClauses(formula.clauses)
    return get_most_occurent_literal(minc)

    

# def unit_propagation(formula):
#     unit_clauses = [c for c in formula.clauses if len(c) == 1]
#     while len(unit_clauses) > 0:
#         unit = unit_clauses[0]
#         print("unit", unit)
#         clauses = [c for c in formula.clauses]
#         print("clauses",clauses)
#         if unit in clauses:
#             assignment = dict(zip(unit,"T"))
#             formula.clauses.remove(unit)
#         print(assignment)
#         indexes = []
#         print("sde",type(formula))
#         for i in range(0, len(formula)):
#             for j in range(0, len(formula.clauses[i])):
#                 if clauses[i][j] == unit:
#                     indexes.append([i, j])
#         for i, j in indexes:
#             formula.remove(clauses[i])
#         unit_clauses = [c for c in formula.clauses if len(c) == 1]
#     return assignment
# def unit_propagation(formula):
#     unit_clauses = [c for c in formula if len(c) == 1]
#     while len(unit_clauses) > 0:
#         unit = unit_clauses[0]
#         print("unit", unit)
#         clauses = [c for c in formula]
#         print("clauses",clauses)
#         if unit in clauses:
#             assignment = dict(zip(unit,"T"))
#             formula.remove(unit)
#         clauses2 = [c for c in clauses if unit not in c]
#         formula = [t for t in formula if clauses2 in t]
#         print("Fr", formula)
#         unit_clauses = [c for c in formula if len(c) == 1]
#     return assignment

def main():
    x = SATSolver('dimacs/rulesets/9-rules.txt', 'dimacs/puzzles/sudoku.txt')
    solution = satisfiable_mom(x.KB)
    print("solution", solution)


if __name__ == '__main__':
    main()