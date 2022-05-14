import random
import typing

from ..element import AbstractElement
from .abstract import AbstractHashingFamily


class StandardHashingFamily(AbstractHashingFamily):
    def __init__(self, functions_n: int, maximum: int):
        """
        Create a new HashingFamily
        Args:
            functions_n: the number of the functions
            maximum: the maximum value that each function must return
        """
        super().__init__(functions_n, maximum)

    def values(self, element: AbstractElement) -> typing.List[int]:
        values: typing.List[int] = []

        for _ in range(self.functions_n):
            value = random.randint(0, self.maximum)
            values.append(value)

        return values
