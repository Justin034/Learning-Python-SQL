import unittest

class TestLearning(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(1, 2)

    def test_equal_2(self):
            self.assertEqual(1, 3)

    def test_always_fails(self):
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()