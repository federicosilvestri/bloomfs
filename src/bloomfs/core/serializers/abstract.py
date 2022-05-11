import abc

from bloomfs.core.containers import AbstractContainer


class AbstractSerializer(abc.ABC):
    """A serializer is a class that given as input an AbstractContainer it serializes it into a file.
    Serializer also does the inverse function: given a resource (file, database, etc) it creates
    an abstract serializer.
    """

    def __init__(self, container: AbstractContainer):
        """
        Initialize the serializer
        Args:
            container: the container to be serialized
        """
        self._container_ = container

    @abc.abstractmethod
    def serialize(self, *args, **kwargs) -> None:
        """
        Serialize the container.
        Args:
            *args: the argument that can be useful to subclass
            **kwargs: the kw-arguments that can be useful to subclass

        Returns: None
        """

    @abc.abstractmethod
    def deserialize(self, *args, **kwargs) -> AbstractContainer:
        """
        Deserialize a resource into an AbstractContainer
        Args:
            *args: the argument that can be useful to subclass
            **kwargs: the kw-arguments that can be useful to subclass

        Returns: AbstractContainer
        """
