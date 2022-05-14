import abc

from bloomfs.core.containers import AbstractContainer
from bloomfs.core.element import AbstractElement


class AbstractFilter(abc.ABC):
    """This class represents the base class for an implementation of BloomFilter."""

    def __init__(self, container: AbstractContainer):
        """
        Create a new filter
        Args:
            container: the abstract container to use to store data
        """
        self.__container__ = container

    @property
    def container(self):
        """
        Property method for container.

        Returns: the AbstractContainer you have chosen for the filter
        """
        return self.__container__

    @abc.abstractmethod
    def put(self, element: AbstractElement) -> None:
        """
        Put the element inside the filter
        Args:
            element: The abstract element

        Returns: None
        """

    @abc.abstractmethod
    def exists(self, element: AbstractElement) -> bool:
        """
        Checks the filter output.
        Args:
            element: the element to check if exists
        Returns: True if filter is positive, false if is negative
        """
