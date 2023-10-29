from typing import Dict
from .Function import Function
from Exceptions import PYLZRException


class KEYWORD:
    functions: Dict[str, Function] = {}

    def clear(self) -> None:
        self.functions.clear()

    def getFunctions(self) -> Dict[str, Function]:
        return self.functions

    def isExists(self, key: str) -> bool:
        return key in self.functions

    def get(self, key: str) -> Function:
        if not self.isExists(key):
            raise PYLZRException("UnknownFunctionException ", "Unknown function " + key)
        return self.functions.get(key)

    def put(self, key: str, function: Function) -> None:
        self.functions[key] = function
