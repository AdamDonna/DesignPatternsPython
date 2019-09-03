import unittest

from .singleton import Singleton


class TestSingletons(unittest.TestCase):
    def test_same_instance(self):
        singletons = [Singleton() for _ in range(5)]
        self.assertEqual(len(set(singletons)), 1)

    def test_singleton_values(self):
        s1 = Singleton()
        s1.value = 10
        s2 = Singleton()
        self.assertEqual(s1.value, s2.value)
