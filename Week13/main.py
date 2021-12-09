# ashton weeks
# awy9n@umsystem.edu
# ALGORITHM: this takes in three functions from a class and then runs unit tests on them to ensure the results
# of the functions are accurate with the correct answers and the math/ formulas are executed correctly. 
# additionally, unit test allows us to see how efficient the program is by timing the time it took for the tests
# to perform.  in order to test, i call the function then compare the results with the answers using .assert calls
# validity of lists passed are checked as well, value errors are raised in the functions as well as the return for 
# math.nan. imports for math.nan and the functions from the other class are called at the beginning here too


import unittest
import Grades
import math

class Grade_Test(unittest.TestCase):
    def test_total_returns_total_of_list(self):
        result = Grades.total([1, 10, 22])
        self.assertEqual(result, 33, "The total function should return 33")
        
    def test_total_returns_total_of_list_two(self):
        result = Grades.total([])
        self.assertEqual(result, 0, "Function should return 0 because a ValueError was raised for empty list")

    def test_average_one(self):
        result = Grades.average([2,5,9])
        self.assertAlmostEqual(result, float(5.33333), 3)

    def test_average_two(self):
        result = Grades.average([2,15,22,9])
        self.assertAlmostEqual(result, 12.0000, 4)

    def test_average_returns_nan(self):
        result = Grades.average([])
        self.assertIs(result, math.nan)
    
    def test_median_one(self):
        result = Grades.median([2,5,1])
        self.assertEqual(result, 2)
    
    def test_median_two(self):
        result = Grades.median([2,5,1,3])
        self.assertEqual(result, 2.5)
    
    def test_value_error_test(self):
        result = Grades.median([])
        with self.assertRaises(ValueError):
            result = Grades.median([])
        try:
            self.assertEqual(result, "Value Error")
        except ValueError:
                return 'Value Error'

__name__ = "__main__"
unittest.main()

# SPECIAL NOTES AND ERROR HANFLING: the third number in almost equal refers to the deciminal places to round both answers to, necessary in functions that
# output floats
