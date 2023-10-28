from typing import List
import ctypes
from ctypes import c_char_p, c_int

from .Token import Token
from .TokenType import TokenType
from utils import types


class Lexer:
    tokens: List[Token]
    code: str
    filename: str
    size: c_int
    pos: c_int
    row: c_int
    col: c_int

    def __init__(self, code: str, filename: str):
        self.tokens = []
        self.code = code
        self.filename = filename
        self.size = c_int(len(code))
        self.pos = c_int(0)
        self.col = self.row = c_int(1)

    def next(self):
        pass

    def pick(self, relativePosition: c_int) -> c_char_p:
        position = c_int(self.pos.value + relativePosition.value)
        if position >= self.size:
            return types.string_to_char('\0')
        return types.string_to_char(self.code[position.value])

    def addToken(self,
                 token_type: TokenType,
                 value: ctypes.c_char_p | None = None
                 ) -> None:
        self.tokens.append(
            Token(
                token_type=token_type,
                value=value
            )
        )
