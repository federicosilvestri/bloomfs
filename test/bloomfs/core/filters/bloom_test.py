import random
import unittest

from bloomfs.core.containers import BoolContainer
from bloomfs.core.filters.bloom import BloomFilter
from bloomfs.core.hashing import StandardHashingFamily


class BloomFilterTest(unittest.TestCase):
    def setUp(self) -> None:
        # create the container
        self.container_size = random.randint(10, 100)
        self.container = BoolContainer(size=self.container_size)

        # create the hashing functions
        self.hashing_ff_n = random.randint(1, 10)
        self.hashing_ff = StandardHashingFamily(
            functions_n=self.hashing_ff_n, maximum=self.container_size
        )

        # create the Bloom Filter
        self.filter = BloomFilter(
            container=self.container, hashing_family=self.hashing_ff
        )

    def test_insert(self):
        self.filter.put()
