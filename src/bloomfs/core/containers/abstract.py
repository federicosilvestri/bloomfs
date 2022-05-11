import abc


class AbstractContainer(abc.ABC):
    """
    This class represents the abstract container for a bloom filter.
    """

    def __init__(self, size: int):
        if size <= 0:
            raise ValueError("The size of container cannot be less or equal than 0")
        self.__size__ = size

    def _check_position_(self, i: int):
        if i < 0 or i >= self.size:
            raise ValueError(
                "The parameter i cannot be less than zero or greater than size of filter"
            )

    @property
    def size(self):
        return self.__size__

    @abc.abstractmethod
    def set(self, i: int) -> None:
        """
        Set the i-th bit to 1.
        Args:
            i: position of bit
        Returns: None
        """

    @abc.abstractmethod
    def get(self, i: int) -> bool:
        """
        Get the i-th bit.i
        Args:
            i: the position of the bit
        Returns: Boolean value: true if bit is set to 1, false if it is set to 0
        """

    @abc.abstractmethod
    def clear(self) -> None:
        """
        Clear the filter: set all bits to 0.
        Returns: None
        """

    @abc.abstractmethod
    def is_full(self) -> bool:
        """
        This method check if filter is full, so it cannot give useful information if you add elements.
        Returns: Boolean value, True if all bits are set to 1, zero if not.
        """

    @abc.abstractmethod
    def __eq__(self, other) -> bool:
        """
        Equality must be implemented
        Args:
            other: Another AbstractContainer to compare

        Returns: True if equal, false if it is not.
        """
