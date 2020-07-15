import unittest
import unicodedata
from fractions import Fraction

class TestSum(unittest.TestCase):
	def test_fractions(self):
		assert isinstance(unicodedata.numeric("¼"),float)

if __name__=="__main__":
	unittest.main()