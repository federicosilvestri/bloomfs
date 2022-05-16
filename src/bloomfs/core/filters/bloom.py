import typing

from bloomfs.core.containers import AbstractContainer
from bloomfs.core.element import AbstractElement
from bloomfs.core.hashing import AbstractHashingFamily

from .abstract import AbstractFilter


class BloomFilter(AbstractFilter):
    """Main implementation of Bloom Filter."""

    def __init__(
        self, container: AbstractContainer, hashing_family: AbstractHashingFamily
    ):
        """
        Create a new Bloom Filter.
        Args:
            container: the container you want to use for this filter
            hashing_family: the family of hashing function
        """
        super().__init__(container)
        self._hashing_family_: AbstractHashingFamily = hashing_family

    @property
    def hashing_family(self) -> AbstractHashingFamily:
        """
        Property method for hashing family.
        Returns: the AbstractHashingFamily object
        """
        return self._hashing_family_

    def put(self, element: AbstractElement) -> None:
        """
        Put an element inside the filter.
        Args:
            element: the element to put
        Returns: None
        """
        # Get the values of hash functions
        values: typing.List[int] = self.hashing_family.values(element)

        for v in values:
            # for each value set the container value to 1
            self.container.set(v)

    def exists(self, element: AbstractElement) -> bool:
        """
        Check if element exists in the filter.
        Args:
            element: the element to check if exists inside container
        Returns: True if element exists, False if element does not exist
        """
        # Get the values of hash functions
        values: typing.List[int] = self.hashing_family.values(element)
        # declare that exists
        exists: bool = True

        # for each value
        for v in values:
            # get the value of container
            filter_value: bool = self.container.get(v)

            if not filter_value:
                # if value is false, it means that the element is not
                # inside filter.
                exists = False
                break

        return exists
