import unittest
from harmony import Harmony
from solve import get_harmony_text, get_path

"""
tests_cases.py provides unit tests for Harmony. More
information regarding the class can be found
in its own file.

Usage
	tests_cases.py

Note
	must be used with inputs provided in cases/

Author
	Menghua Wu
Version
	May 23, 2016
"""

class TestHarmonyCases(unittest.TestCase):
	################################
	# 2 x 2 Trivial Case
	################################
	def testSmall_1(self):
		"""
		testSmall_1
			tests the correct path for a 2 x 2. Trivial
			test case for debugging.
		"""
		actual_length = 1
		path = get_path("cases/1.in")

		self.assertEqual(actual_length, len(path))

	################################
	# 3 x 3 Small Cases
	################################
	def testMedium_1(self):
		"""
		testMedium_1
			tests the correct path for a 3 x 3. Trivial
			test case for debugging.
		"""
		actual_length = 2
		path = get_path("cases/2.in")

		self.assertEqual(actual_length, len(path))

	def testMedium_2(self):
		"""
		testMedium_2
			tests the correct path for a 3 x 3. Harmony 3
			puzzle 1 of pack 1.
		"""
		actual_length = 5
		path = get_path("cases/3.in")

		self.assertEqual(actual_length, len(path))

	def testMedium_3(self):
		"""
		testMedium_3
			tests the correct path for a 3 x 3. Harmony 3
			puzzle 1 of 2015 holiday pack.
		"""
		actual_length = 5
		path = get_path("cases/4.in")

		self.assertEqual(actual_length, len(path))

	def testMedium_4(self):
		"""
		testMedium_4
			tests for an invalid path for a 3 x 3.
		"""
		path = get_path("cases/5.in")

		assert path is None

	def testLarge_1(self):
		"""
		testLarge_1
			tests for a trivial path for a 4 x 4.
		"""
		actual_length = 4
		path = get_path("cases/6.in")

		self.assertEqual(actual_length, len(path))

	def testLarge_2(self):
		"""
		testLarge_2
			tests for a trivial path for a 4 x 4.
		"""
		actual_length = 12
		path = get_path("cases/7.in")

		self.assertEqual(actual_length, len(path))

	def testLarge_3(self):
		"""
		testLarge_3
			tests for a trivial path for Harmony 3
			puzzle 8 of pack 1.
		"""
		actual_length = 11
		path = get_path("cases/8.in")

		self.assertEqual(actual_length, len(path))

if __name__ == '__main__':
	unittest.main()