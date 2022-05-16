import random
import typing

import numpy as np

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
        self.functions_n = typing.List[typing.Callable[[int], int]]
        self._generate_functions_()

    def _generate_prime_numbers_(self):
        if self.maximum < 6:
            return [2, 3, 5]

        sieve = np.ones(self.maximum // 3 + (self.maximum % 6 == 2), dtype=bool)
        for i in range(1, int(self.maximum ** 0.5) // 3 + 1):
            if sieve[i]:
                k = 3 * i + 1 | 1
                sieve[k * k // 3::2 * k] = False
                sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False
        return np.r_[2, 3, ((3 * np.nonzero(sieve)[0][1:] + 1) | 1)]

    def _generate_functions_(self):
        for _ in range(self.functions_n):


    # find a prime number < maximum

    def values(self, element: AbstractElement) -> typing.List[int]:
        values: typing.List[int] = [
            random.randint(0, self.maximum) for _ in range(0, self.functions_n)
        ]

        return values
