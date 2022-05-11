import random
import unittest
from pathlib import Path

from bloomfs.core.containers import AbstractContainer, BoolContainer
from bloomfs.core.serializers import PickleSerializer


class TestPickleSerializer(unittest.TestCase):
    def setUp(self) -> None:
        self.size = random.randint(1, 1000)
        self.container: AbstractContainer = BoolContainer(size=1000)

        positions = random.choices(range(0, self.size), k=int(self.size / 2))
        for p in positions:
            self.container.set(p)
        self.file_path = Path("/tmp/test.dump")

    def test_serialize(self):
        serializer = PickleSerializer(self.container)
        serializer.serialize(file_path=self.file_path)
        deserialized_container = serializer.deserialize(filepath=self.file_path)
        self.assertEqual(self.container, deserialized_container)
