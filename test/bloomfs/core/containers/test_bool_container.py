import random
import unittest

from bloomfs.core.containers import BoolContainer


class BoolContainerTest(unittest.TestCase):
    def test_init(self):
        for i in range(-10, 0):
            with self.assertRaises(ValueError):
                BoolContainer(size=i)

    def setUp(self) -> None:
        self.size = random.randint(1, 10000)
        self.instance = BoolContainer(self.size)

    def test_set_get_invalid(self):
        for s in [-1, self.size]:
            with self.assertRaises(ValueError):
                self.instance.set(s)
                self.instance.set(s)

    def test_set_get_valid(self):
        # position to set to 1
        positions = [
            i for i in random.choices(range(0, self.size), k=int(self.size / 2))
        ]
        for p in positions:
            self.instance.set(p)

        for i in range(0, self.size):
            expected = i in positions
            actual = self.instance.get(i)
            self.assertEqual(expected, actual)

    def test_full(self):
        self.assertFalse(self.instance.is_full())
        for i in range(0, self.size):
            self.instance.set(i)
        self.assertTrue(self.instance.is_full())

    def test_clear(self):
        for i in range(0, self.size):
            self.instance.set(i)

        self.instance.clear()
        for i in range(0, self.size):
            self.assertFalse(self.instance.get(i))

    def test_eq(self):
        with self.assertRaises(TypeError):
            self.instance == 1
        self.assertTrue(self.instance == self.instance)
        self.assertFalse(self.instance == BoolContainer(size=10))
