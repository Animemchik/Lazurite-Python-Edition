class PYLZRException(Exception):
    def __init__(self, type_: str, text: str):
        super().__init__()
        self.type_: str = type_
        self.text: str = "\u001b[31m" + text

    def getType(self) -> str:
        return self.type_

    def getText(self) -> str:
        return self.text
