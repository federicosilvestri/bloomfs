import typing

from .abstract import AbstractContainer


class BoolContainer(AbstractContainer):
    """This class represents a bool container for bloom filter. The representation
    is given by an array of boolean value. The size of array is immutable."""

    def __init__(self, size: int):
        """
        Initialize the Bool container object. It creates an array of
        boolean values all set to False
        Args:
            size: the size of filter
        """
        super().__init__(size)
        self.__bloom__: typing.List[bool] = [False for _ in range(size)]

    def set(self, i: int) -> None:
        """
        Set the i-th position of filter to True value
        Args:
            i: the position to set to True

        Returns: None
        """
        self._check_position_(i)
        self.__bloom__[i] = True

    def get(self, i: int) -> bool:
        """
        Check if the i-th position of Bloom filter is set to True
        Args:
            i: the position to check
        Returns: the content of i-th position of bool array
        """
        self._check_position_(i)
        return self.__bloom__[i]

    def clear(self) -> None:
        """
        Clear the filter, set all array to False values.
        Returns: None
        """
        self.__bloom__ = [False for _ in range(self.size)]

    def is_full(self) -> bool:
        """
        Check if filter is full.
        Returns: True if exists at least one position to False value, False if all position are set to True
        """
        return False not in self.__bloom__

