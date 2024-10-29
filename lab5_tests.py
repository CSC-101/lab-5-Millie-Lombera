import data
import lab5
import unittest
import data
from data import Point
from lab5 import time_add, is_descending, largest_between, furthest_from_origin


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.
        #DONE
    # Part 2
    #    Part 2 tests should be in data_tests.py.
        #DONE
    # Part 3
    def test_timeAdd1(self):
        time1 = data.Time(2,4,5)
        time2 = data.Time(4,2,0)
        self.assertEqual(data.Time(6,6,5),time_add(time1, time2))

    def test_timeAdd2(self):
        time1 = data.Time(8,30,24)
        time2 = data.Time(8,32,40) #minute:22 seconds:31
        result = data.Time(17,3,4)
        print(result == data.Time(17,3,4))
        self.assertEqual(lab5.time_add(time1, time2),result)

    # Part 4
    def test_isdecending1(self):
        list1 = is_descending([5.2,4.0,2.22,1.11,])
        self.assertEqual(list1,True)

    def test_isdecending2(self):
        list2 = is_descending([1.0, 2.0, 2.2, 3])
        self.assertEqual(list2,False)

    # Part 5
    def test_largestinbetween1(self):
        test1 = largest_between([3, 5, 7, 2, 8], 1, 3)
        self.assertEqual(test1,2)

    def test_largestinbetween2(self):
        test2 = largest_between([3, 5, 7, 2, 8], 3, 1)
        self.assertEqual(test2,None)
        test3 = largest_between([3, 5, 7, 2, 8], -3, 3)
        self.assertEqual(test3,None)

    # Part 6
    def test_furthestfromorigin1(self):
        points1 = [Point(1, 1), Point(2, 2), Point(3, 3), Point(0, 5)]
        self.assertEqual(furthest_from_origin(points1),3)

        points2 = [Point(0, 0), Point(0, 0), Point(0, 0)]
        self.assertEqual(furthest_from_origin(points2),0)

    def test_furthestfromorigin2(self):
        points1 = [Point(3, 4)]
        points2 = [Point(3, 4), Point(-3, -4)]
        self.assertEqual(furthest_from_origin(points1),0)
        self.assertEqual(furthest_from_origin(points2),0)

if __name__ == '__main__':
    unittest.main()
