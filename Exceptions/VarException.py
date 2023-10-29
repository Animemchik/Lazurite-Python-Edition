class VarException(Exception):
    def __init__(self, variable: str):
        super().__init__(f"Variable {variable} does not exists")
        self.variable: str = variable

    def getVariable(self) -> str:
        return self.variable
