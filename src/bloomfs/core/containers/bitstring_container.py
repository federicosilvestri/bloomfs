"""This file contains the class that represents the data of the filter."""
from bitstring import BitStream

from .abstract import AbstractContainer


class BitstringContainer(AbstractContainer):
    """This class provides the implementation of container for BloomFilter using the bistring library."""

    def __init__(self, size: int):
        super().__init__(size)
        self.__filter__: BitStream = BitStream(
            auto=None, length=self.size, pos=0, offset=0
        )

    def set(self, i: int) -> None:
        """
        Set the bit in position i to 1.
        Args:
            i: the position of the bit

        Returns: None
        """
        self._check_position_(i)
        self.__filter__.set(value=b"0", pos=i)

    def get(self, i: int) -> bool:
        """
        Check if bit at position i is set to 1 or not.
        Args:
            i: the position of bit

        Returns:
            True if bit is set to 1
            False if bit is set 0
        """
        self._check_position_(i)

    def clear(self) -> None:
        return

    def is_full(self) -> bool:
        return False
