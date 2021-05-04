import unittest
from avglist import *

class avglist_test(unittest.Testcase):
	def empty_list(self):
		assert len(function_returns_list())==0, "list empty"

	def divide_zero(self):
		self.assertRaises(ValueError)

	def correct_avg(self):
		self.assertEqual(avglist([1,2,3,4,5,6]),3.5)

if __name__ == '__main__':
	unitTest.main() 
