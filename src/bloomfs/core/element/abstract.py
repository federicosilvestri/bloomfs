import abc


class AbstractElement(abc.ABC):
    """This class represents an element that can be put inside a Bloom Filter."""

    @abc.abstractmethod
    def to_int(self) -> int:
        """
        This is the method that converts the element inside an integer.
        For example if you have a document, it can return the document ID.
        Returns: Integer value
        """
