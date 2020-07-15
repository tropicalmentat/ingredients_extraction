import unittest
from fractions import Fraction

class TestSum(unittest.TestCase):
	def test_fractions(self):
		assert isinstance("¼",Fraction)

if __name__=="__main__":
	unittest.main()