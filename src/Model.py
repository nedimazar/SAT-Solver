class Model:

    def __init__(self):
        self.__variables = self.generate_variables()

    #OVERRIDE THIS FOR OTHER PROBLEMS
    def generate_variables(self):
        variables = {}
        for x in range(1, 10):
            for y in range(1, 10):
                for v in range(1, 10):
                    variables[f"{x}{y}{v}"] = None
        return variables

    def get_variables(self):
        return self.__variables
    
    def push(self, variable, assignment=None):
        self.__variables[variable] = assignment
    
    def flip(self, variable):
        if variable in self.__variables and self.__variables[variable] is not None:
            self.__variables[variable] = not self.__variables[variable]