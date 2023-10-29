from abc import ABC, abstractmethod
from ctypes import c_double, c_int
from typing import List


class Value(ABC):
    @abstractmethod
    def raw(self) -> object: ...

    @abstractmethod
    def asInt(self) -> c_int: ...

    @abstractmethod
    def asNumber(self) -> c_double: ...

    @abstractmethod
    def asString(self) -> str: ...

    @abstractmethod
    def asArray(self) -> List[c_int]: ...

    @abstractmethod
    def type(self) -> c_int: ...
