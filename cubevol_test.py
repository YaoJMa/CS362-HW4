import unittest
from cubevol import *


class TestCube(unittest.TestCase):	
	def setUp(self):
		self.cube_vol = ['2']

	def test_vol(self):
		self.assertEqual(cube_vol(2),8)
		self.assertEqual(cube_vol(1),1)
		self.assertEqual(cube_vol(0),0)
		self.assertEqual(cube_vol(5.5),166.375)
		
	def test_input_value(self):
		self.assertRaises(TypeError, cube_vol, True)

if __name__ == '__main__':
	unittest.main()
