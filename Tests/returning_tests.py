import unittest
import return_addtion
import triangle_area

class MyTestCase(unittest.TestCase):

    def test_return_addtion(self):

        self.assertEqual(15, return_addtion.add_two(7, 8))
        self.assertEqual(45, return_addtion.add_two(40, 5))
        # Add two more tests of your own below here
        self.assertEqual(-6, return_addtion.add_two(-12,6))
        self.assertEqual(-3, returm_addition.add_two(-2,-1))
    def test_triangle_area(self):
        self.assertEqual(6.0, triangle_area.area(3, 4, 5))


if __name__ == '__main__':
    unittest.main()
