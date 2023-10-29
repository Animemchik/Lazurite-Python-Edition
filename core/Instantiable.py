from abc import ABC, abstractmethod
from runtime import Value
from typing import List


class Instantiable(ABC):
    @abstractmethod
    def newInstance(self, args: List[Value]) -> Value: ...
