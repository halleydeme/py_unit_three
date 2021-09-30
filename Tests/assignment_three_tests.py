import unittest
from assignment_three import surface_area
from assignment_three import area_of_rectangle




class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(10, area_of_rectangle(5,2))
        self.assertEqual(12, area_of_rectangle(4,3))
        self.assertEqual(150, surface_area(4,3,9))
        self.assertEqual(72, surface_area(3,2,6))
if __name__ == '__main__':
    unittest.main()
