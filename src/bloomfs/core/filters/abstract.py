import abc

from bloomfs.core.containers import AbstractContainer


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
    def put(self, element: int) -> None:
        """
        Put the element inside the filter
        Args:
            element: integer number that can represent anything. For example and ID, a documentID, or a hashed URL.

        Returns: None
        """

    @abc.abstractmethod
    def exists(self, element: int) -> bool:
        """
        Checks the filter output.
        Args:
            element: the element to check if exists
        Returns: True if filter is positive, false if is negative
        """
