from Literal import Literal
class KB:

    def __init__(self, clauses) -> None:
        self.clauses = clauses
        self.clauses_copy = None
        self.longest = None
        self.pure_index = None
        self.pure_dict = None
        self.unit_index = None
        self.magic(clauses)
    
    def __len__(self):
        return len(self.clauses)

    def contains_unit_clauses(self):
        return len(self.unit_index) > 0
    def contains_pure_literal(self):
        return  len(self.pure_literals) > 0

    def next_p(self):
        if self.contains_unit_clauses():
            return self.get_next_unit_clause()
        if self.contains_pure_literal():
            return self.get_next_pure_literal()

    def get_next_unit_clause(self):
        return self.clauses_copy[self.unit_index.pop()][0]
    def get_next_pure_literal(self):
        return self.pure_literals.pop()

    def magic(self, clauses):
        longest = 0
        shortest_index = {}
        pure_literals = []
        unit_index = []
        literal_set = set()

        save = []

        for i, clause in enumerate(clauses):
            save.append([])
            if len(clause) in shortest_index:
                shortest_index[len(clause)].append(clause)
            else:
                shortest_index[len(clause)] = [clause]
            if len(clause) > longest:
                longest = len(clause)

            if len(clause) == 1:
                unit_index.append(i)
            for j, literal in enumerate(clause):
                save[i].append(literal)

                pure_literals.append(literal)

        for x in set(pure_literals):
            if x in pure_literals and -x in pure_literals:
                while x in pure_literals:
                    pure_literals.pop(pure_literals.index(x))
                while -x in pure_literals:
                    pure_literals.pop(pure_literals.index(-x))
                
                
                    
        self.clauses_copy = save
        self.longest = longest
        self.pure_literals = pure_literals
        self.unit_index = unit_index
        

if __name__ == "__main__":
    clauses = [[Literal(True, 'a'), Literal(True, 'b')], [Literal(True, 'c')], [Literal(False, 'b'), Literal(True, 'a')], [Literal(True, 'y')]]
    k = KB(clauses)


    print(k.next_p())
    print(k.next_p())
    print(k.next_p())
    print(k.next_p())
    print(k.next_p())
    print(k.next_p())
    print(k.next_p())
    print(k.next_p())
  






    '''
    a = [[Literal(True, 'a'), Literal(True, 'b')], [Literal(False, 'b'), Literal(True, a)]]
    
    
    
    '''



