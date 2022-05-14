import abc
import typing

from bloomfs.core.element import AbstractElement


class AbstractHashingFamily(abc.ABC):
    """This class represents an abstract for a hashing function family."""

    def __init__(self, functions_n: int, maximum: int):
        """
        Create a new HashingFamily
        Args:
            functions_n: the number of the functions
            maximum: the maximum value that each function must return
        """
        if functions_n <= 0:
            raise ValueError("The functions_n parameter must be > 0!")
        if maximum <= 0:
            raise ValueError("The maximum must be > 0!")

        self.__functions_n__ = functions_n
        self.__maximum__ = maximum

    @property
    def functions_n(self) -> int:
        """
        Property for functions_n field
        Returns: int value that represents the number of functions to create
        """
        return self.__functions_n__

    @property
    def maximum(self) -> int:
        """
        Property for maximum field.
        Returns: int value that represents the number maximum value that hashing function can assume
        """
        return self.__maximum__

    @abc.abstractmethod
    def values(self, element: AbstractElement) -> typing.List[int]:
        """
        Returns a list of values that the hashing functions has computed, given as input an abstract element.
        Args:
            element: the abstract element to compute the hashing function

        Returns: a list of integer values that represents the position of filter to set.
        """
