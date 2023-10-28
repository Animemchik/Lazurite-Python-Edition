import ctypes
from .TokenType import TokenType
from utils.types import char_to_string


class Token(ctypes.Structure):
    _fields_ = [("token_type", TokenType), ("value", ctypes.c_char_p)]

    def getTokenType(self) -> TokenType:
        return self.token_type

    def getValue(self) -> ctypes.c_char_p | None:
        return self.value

    def __str__(self) -> str:
        if self.value:
            return f"{self.token_type.name()} = {char_to_string(self.value)}"
        return f"{self.token_type.name()}"
