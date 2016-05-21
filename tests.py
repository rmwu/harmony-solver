import unittest
from harmony import Harmony

"""
tests.py provides unit tests for the Harmony.
More information regarding the class can be found
in its own file.

Usage
	tests.py 

Author
	Menghua Wu
Version
	May 21, 2016
"""

class TestHarmonySmall(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		"""
		constructor
			initializes and stores a 2 by 2 game of
			Harmony for use in tests
		"""
		super(TestHarmonySmall,
		    self).__init__(*args, **kwargs)

		n = 2
		colors = [0,1,1,0]
		swaps = [0,1,0,1]
		self.harmony = Harmony(n, colors, swaps)

	################################
	# Testing index manipulations
	################################
	def testIndexManip_list_to_grid_index_1(self):
		"""
		testIndexManip_list_to_grid_index_1
			tests method list_to_grid_index to ensure
			that indices are being property translated
			from list to grid, for the corner of the grid.
		"""
		index = 3
		grid_coords = (1, 1)

		self.assertEqual(grid_coords,
		                self.harmony.list_to_grid_index(index))

	def testIndexManip_list_to_grid_index_2(self):
		"""
		testIndexManip_list_to_grid_index_2
			tests method list_to_grid_index to ensure
			that indices are being property translated
			from list to grid, for an intermediate element
			in the grid
		"""
		index = 2
		grid_coords = (1, 0)

		self.assertEqual(grid_coords,
		                self.harmony.list_to_grid_index(index))

	def testIndexManip_grid_to_list_index_1(self):
		"""
		testIndexManip_grid_to_list_index_1
			tests method grid_to_list_index to ensure
			that indices are being property translated
			from grid to list, for the corner of the grid
		"""
		index = 2
		g = (1, 0)

		self.assertEqual(index,
		                self.harmony.grid_to_list_index(g[0], g[1]))

	def testIndexManip_grid_to_list_index_2(self):
		"""
		testIndexManip_grid_to_list_index_2
			tests method grid_to_list_index to ensure
			that indices are being property translated
			from grid to list, for an intermediate element
			in the grid
		"""
		index = 3
		g = (1, 1)

		self.assertEqual(index,
		                self.harmony.grid_to_list_index(g[0], g[1]))

	################################
	# Testing Harmony constructor
	################################
	def testConstructor_n(self):
		"""
		testConstructor_n
			tests whether Harmony creates an object
			knowing its correct size
		"""
		n = 2
		self.assertEqual(n, self.harmony.n)

	def testConstructor_grid(self):
		"""
		testConstructor_grid
			tests whether Harmony initializes the grid
			correctly, with (color, swaps) pairs
		"""
		grid = [[(0,0), (0,1)],
				[(1,0), (1,1)]]

		self.assertEqual(grid, self.harmony.grid)

	def testConstructor_grid_size(self):
		"""
		testConstructor_grid_size
			tests whether Harmony initializes the grid
			with the correct size
		"""
		self.assertEqual(2, len(self.harmony.grid))
		self.assertEqual(2, len(self.harmony.grid[0]))

	def testConstructor_swaps_left(self):
		"""
		testConstructor_swaps_left
			tests whether Harmony records the correct
			number of swaps available upon creation
		"""
		self.assertEqual(2, self.harmony.swaps_left)

	def testConstructor_starting_points_none(self):
		"""
		testConstructor_starting_points_none
			tests that Harmony extracts the correct
			starting points, given that there are none
		"""
		n = 2
		colors = [0,1,1,0]
		swaps = [0,0,0,0]
		harmony = Harmony(n, colors, swaps)

		starting_points = set()

		self.assertEqual(starting_points, set(harmony.starting_points))

	def testConstructor_starting_points_exist(self):
		"""
		testConstructor_starting_points_exist
			tests that Harmony extracts the correct
			starting points, given that they exist
		"""
		starting_points = set([(0,1), (1,1)])

		self.assertEqual(starting_points, set(self.harmony.starting_points))

if __name__ == '__main__':
	unittest.main()