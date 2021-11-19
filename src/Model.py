class Model:
        def __init__(self, formula, model = None):
            self.formula = formula
            if model:
                self.model = model
            else:
                self.model = self.get_model(formula)
        
        def __str__(self):
            return str(self.model)

        def get_model(self, formula):
            model = {}
            for literal in self.flatten(formula):
                if literal.abs() not in model:
                    model[literal.abs()] = None
            return model

        def flatten(self, nested):
            return [item for sublist in nested for item in sublist]

        def next_unassigned(self):
            for x in self.model:
                if self.model[x] == None:
                    return x
                    

        def union(self, literal):
            if literal:
                self.model[literal.abs()] = not literal.negated
            return Model(self.formula, self.model)
