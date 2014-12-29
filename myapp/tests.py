from django.test import TestCase
import random
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.size = 200

    def test_lenth(self):
        random.shuffle(self.size)
        self.assertEqual(self.size, 200)

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        element = random.choice(self.size)
        self.assertTrue(element in self.size)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.size, 20)
        for element in random.sample(self.size, 5):
            self.assertTrue(element in self.size)

if __name__ == '__main__':
    unittest.main()

