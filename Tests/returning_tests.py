import unittest
import return_addtion
import triangle_area

class MyTestCase(unittest.TestCase):

    def test_return_addtion(self):

        self.assertEqual(15, return_addtion.add_two(7, 8))
        self.assertEqual(45, return_addtion.add_two(40, 5))
        # Add two more tests of your own below here
        self.assertEqual(-6, return_addtion.add_two(-12,6))
        self.assertEqual(-3, return_addtion.add_two(-2,-1))
    def test_triangle_area(self):
        self.assertEqual(6.0, triangle_area.area(3, 4, 5))
        self.assertEqual(26.832815729997478, triangle_area.area(7,8,9))
        self.assertEqual(14.696938456699069, triangle_area.area(5,6,7))


if __name__ == '__main__':
    unittest.main()
