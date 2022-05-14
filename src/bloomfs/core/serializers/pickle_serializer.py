import pickle
import typing
from pathlib import Path

from ..containers import AbstractContainer
from .abstract import AbstractSerializer


class PickleSerializer(AbstractSerializer):
    """This class is a serializer that uses python Pickle library."""

    def serialize(self, **kwargs) -> None:
        """
        Serialize a container.
        Args:
            **kwargs:
                file_path: the file path where write the container

        Returns: None
        """
        file_path: Path = typing.cast(Path, kwargs.get("file_path"))
        pickle.dump(self._container_, file=file_path.open("wb"))

    def deserialize(self, **kwargs) -> AbstractContainer:
        """
        Deserialize a container.
        Args:
            **kwargs:
                filepath: the file path where read the container

        Returns: The AbstractContainer
        """
        file_path: Path = typing.cast(Path, kwargs.get("file_path"))
        container = pickle.load(file=file_path.open("rb"))
        return typing.cast(AbstractContainer, container)
