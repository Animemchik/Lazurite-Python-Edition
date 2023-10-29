from abc import ABC, abstractmethod
from runtime import Value


class Function(ABC):
    @abstractmethod
    def execute(self, *args: Value) -> Value: ...
