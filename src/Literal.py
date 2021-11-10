class Literal:

    def __init__(self, negated, symbol, truth=None):
        self.negated = negated
        self.symbol = symbol
        self.truth = truth
    
    def __repr__(self):
        tail = ""
        if self.truth:
            tail = f": {'T' if self.truth else 'F'}"
        negated = "-" if self.negated else ""
        return(f"{negated}{self.symbol}{tail}")

