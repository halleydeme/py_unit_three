import unittest
import assignment_three



class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(10, assignment_three.area_of_rectangle(5,2))
        self.assertEqual(12,assignment_three.area_of_rectangle(4,3))
        self.assertEqual(150, assignment_three.surface_area(4,3,9))
        self.assertEqual(72, assignment_three.surface_area(3,2,6))
if __name__ == '__main__':
    unittest.main()
