import unittest
import assignment_three


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(10, assignment_three.area_of_rectangle(5,2))
        self.assertEqual(30, assignment_three.surface_area(5,2,3))
if __name__ == '__main__':
    unittest.main()
