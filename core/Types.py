from ctypes import c_int
from typing import List


class Types:
    OBJECT: c_int   = c_int(0)
    NUMBER: c_int   = c_int(1)
    STRING: c_int   = c_int(2)
    ARRAY: c_int    = c_int(3)
    MAP: c_int      = c_int(4)
    FUNCTION: c_int = c_int(5)
    CLASS: c_int    = c_int(6)

    FIRST: c_int    = OBJECT
    LAST: c_int     = CLASS

    NAMES: List[str] = ["object", "number", "string", "array", "map", "function", "class"]

    @staticmethod
    def typeToString(self, type_: c_int) -> str:
        if self.FIRST <= type_ <= self.LAST:
            return self.NAMES[type_]
        return "unknown (" + str(type_.value) + ")"
