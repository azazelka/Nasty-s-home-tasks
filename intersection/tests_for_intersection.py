import unittest

import intersection


class TestIntersection(unittest.TestCase):
    def test_no_intersections(self):
        array1 = [1, 2, 4, 5]
        array2 = [3, 3, 3, 3, 3]

        self.assertEqual(list(intersection.intersection(array1, array2)), [])

    def test_intersection_extreme_elements(self):
        array1 = [1, 9]
        array2 = [1, 3, 3, 3, 3, 9]
        self.assertEqual(list(intersection.intersection(array1, array2)), [1, 9])

    def test_intersection_full(self):
        array1 = [3, 3, 3, 3, 7, 7, 9, 9, 12, 12]
        array2 = [3, 3, 3, 3, 7, 7, 9, 9, 12, 12]
        self.assertEqual(list(intersection.intersection(array1, array2)), array1)

    def test_intersection_partial(self):
        array1 = [1, 3, 3, 3, 3, 9]
        array2 = [1, 10]
        self.assertEqual(list(intersection.intersection(array1, array2)), [1])

    def test_intersection_empty_array(self):
        array1 = [1]
        array2 = []
        self.assertEqual(list(intersection.intersection(array1, array2)), [])

    def test_intersection_no_iterable(self):
        array1 = 1
        array2 = 1
        self.assertRaises(TypeError, intersection, array1, array2)

    def test_intersection_type_error(self):
        array1 = {1: 1, 2: 2}
        array2 = {1: 1, 2: 2}

        self.assertRaises(TypeError, intersection, array1, array2)


if __name__ == '__main__':
    unittest.main()
