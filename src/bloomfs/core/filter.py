"""This file contains the class that represents the data of the filter."""
from bitstring import BitStream


class BloomFilterContainer:
    def __init__(self, size: int):
        if size < 0:
            raise ValueError("The filter size must be greater than 0")
        self.__size__: int = size
        self.__filter__: BitStream = BitStream(
            auto=None, length=self.size, pos=0, offset=0
        )

    @property
    def size(self) -> int:
        """
        Property for
        Returns:

        """
        return self.__size__

    def __check_index_parameter__(self, i: int) -> None:
        if i < 0 or i >= (self.size - 1):
            raise ValueError(
                "The i parameter cannot be less than 0 or more than size-1"
            )

    def set(self, i: int) -> None:
        """
        Set the bit in position i to 1.
        Args:
            i: the position of the bit

        Returns: None
        """
        self.__check_index_parameter__(i)

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
        self.__check_index_parameter__(i)
