import unittest
import calc

class test_calc(unittest.TestCase):
    def test_add(self):
        test = calc.add(15, 3)
        self.assertEqual(test, 18)

    def test_sub(self):
        test = calc.sub(15, 3)
        self.assertEqual(test, 12)

    # def test_equal_2(self):
    #         self.assertEqual(1, 3)

    # def test_always_fails(self):
    #     self.assertFalse(False)

    def test_word(self):
        self.assertIn("Pen".capitalize(), "Penis")

    def test_div(self):
        self.assertRaises(ValueError, calc.div, 9, 0)
        with self.assertRaises(ValueError):
            calc.div(10, 0)

if __name__ == '__main__':
    unittest.main()