import pickle
from pathlib import Path

from ..containers import AbstractContainer
from .abstract import AbstractSerializer


class PickleSerializer(AbstractSerializer):
    """This class is a serializer that uses python Pickle library."""

    def serialize(self, file_path: Path, *args, **kwargs) -> None:
        """
        Serialize a container.
        Args:
            file_path: the file path where write the container
            *args:
            **kwargs:

        Returns: None
        """
        pickle.dump(self._container_, file=file_path.open("wb"))

    def deserialize(self, filepath: Path, *args, **kwargs) -> AbstractContainer:
        """
        Deserialize a container.
        Args:
            filepath: the file path where read the container
            *args:
            **kwargs:

        Returns: The AbstractContainer
        """
        return pickle.load(file=filepath.open("rb"))
