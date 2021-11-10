class Literal:
    """Literal class for holding symbols with assigned values.
    """
    def __init__(self, negated=False, symbol=None):
        """Constructor for Literal class.

        Args:
            negated (bool, optional): Wether the symbol is negated or not. Defaults to False.
            symbol (string, optional): The symbol of the literal, could be any variable name. Defaults to None.
            truth (bool, optional): If the truth value of the literal, leave blank if not known yet. Defaults to None.
        """
        self.negated = negated
        self.symbol = symbol
        #self.truth = truth
    
    def __hash__(self):
        return hash(f"{self.negated}, {self.symbol}")

    def __eq__(self, o):
        if isinstance(o, type(self)):
            return self.negated == o.negated and self.symbol == o.symbol ##and self.truth == o.truth

    def __repr__(self):
        tail = ""
        '''
        if self.truth:
            tail = f": {'T' if self.truth else 'F'}"
        '''
        negated = "-" if self.negated else ""
        return(f"{negated}{self.symbol}{tail}")

    def __neg__(self):
        return Literal(not self.negated, self.symbol)
'''
class Axiom(Literal):
    """The Axiom class is identical to the Literal class, we use this nomenclature to differenciate between literals that are given to be true and literals for which the truth value is to be determined. The truth value of an Axiom is static.
    """
    def __init__(self, negated=False, symbol=None, truth=None):
        super().__init__(negated=negated, symbol=symbol, truth=truth)

'''