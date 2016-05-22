import unittest
from random import randint
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
		grid = [[(0,0), (1,1)],
				[(1,0), (0,1)]]

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
		index = 3
		g = (1, 1)

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
		index = 2
		g = (1, 0)

		self.assertEqual(index,
		                self.harmony.grid_to_list_index(g[0], g[1]))

	def testIndexManip_valid_index_origin(self):
		"""
		testIndexManip_valid_index_origin
			tests method valid_index, given the origin
		"""
		index = 0

		self.assertTrue(self.harmony.valid_index(index))

	def testIndexManip_valid_index_arbitrary(self):
		"""
		testIndexManip_valid_index_arbitrary
			tests method valid_index, given an arbitrary,
			non-boundary, valid index
		"""
		index = randint(1, 2)

		self.assertTrue(self.harmony.valid_index(index))

	def testIndexManip_valid_index_last(self):
		"""
		testIndexManip_valid_index_last
			tests method valid_index, given the last valid
			index
		"""
		index = 3

		self.assertTrue(self.harmony.valid_index(index))

	def testIndexManip_invalid_index_before(self):
		"""
		testIndexManip_invalid_index_before
			tests method valid_index, given a negative, invalid
			index
		"""
		index = -1

		self.assertFalse(self.harmony.valid_index(index))

	def testIndexManip_invalid_index_after(self):
		"""
		testIndexManip_invalid_index_before
			tests method valid_index, given a negative, invalid
			index
		"""
		index = 5

		self.assertFalse(self.harmony.valid_index(index))

	def testIndexManip_indices_in_line_horizontal(self):
		"""
		testIndexManip_indices_in_line_horizontal
			tests whether two horizontal colinear indices are
			reported as in line with each other
		"""
		index1 = (0, 0)
		index2 = (0, 1)

		self.assertTrue(self.harmony.indices_in_line(index1, index2))

	def testIndexManip_indices_in_line_vertical(self):
		"""
		testIndexManip_indices_in_line_vertical tests
			whether two vertical colinear indices are
			reported as in line with each other
		"""
		index1 = (0, 0)
		index2 = (1, 0)

		self.assertTrue(self.harmony.indices_in_line(index1, index2))

	def testIndexManip_indices_in_line_nonlinear(self):
		"""
		testIndexManip_indices_in_line_nonlinear
			tests whether two non-linear indices are
			reported as in not line with each other
		"""
		index1 = (0, 0)
		index2 = (1, 1)

		self.assertFalse(self.harmony.indices_in_line(index1, index2))

	################################
	# Testing basic getter / setter
	################################
	def testBasic_get(self):
		"""
		testBasic_get
			tests whether Harmony can retrieve correct
			values, given a list index
		"""
		index = 3
		value = (0, 1)

		self.assertEqual(value, self.harmony.get(index))

	def testBasic_set_value(self):
		"""
		testBasic_get
			tests whether Harmony can set correct values
			given a list index and value
		"""
		index = 3
		old_value = self.harmony.get(index)
		value = (1, 1)

		# should not be equal before setting
		self.assertNotEqual(value, self.harmony.get(index))

		self.harmony.set_value(index, value)
		
		# should be equal after setting
		self.assertEqual(value, self.harmony.get(index))

		# restore the original grid
		self.harmony.set_value(index, old_value)

	################################
	# Testing game logic
	################################
	def testLogic_valid_swap(self):
		"""
		testLogic_valid_swap
			tests whether a valid swap is reported as valid
		"""
		index1 = (0, 1)
		index2 = (1, 1)

		self.assertTrue(self.harmony.valid_swap(index1, index2))

	def testLogic_invalid_swap(self):
		"""
		testLogic_invalid_swap
			tests whether a invalid swap is reported as 
			not valid
		"""
		index1 = (0, 0)
		index2 = (1, 0)

		self.assertFalse(self.harmony.valid_swap(index1, index2))

	def testLogic_has_swaps_left_true(self):
		"""
		testLogic_has_swaps_left_true
			tests whether swaps_left, given a positive number of
			remaining total swaps, returns True
		"""
		self.assertTrue(self.harmony.has_swaps_left())

	def testLogic_has_waps_left_none(self):
		"""
		testLogic_has_waps_left_none
			tests whether swaps_left, given no remaining total
			swaps, returns False
		"""
		n = 2
		colors = [0,0,1,1]
		swaps = [0,0,0,0]
		harmony = Harmony(n, colors, swaps)

		self.assertFalse(harmony.has_swaps_left())

	def testLogic_game_unsolved(self):
		"""
		testLogic_game_unsolved
			tests whether an unsolved game is reported as unsolved
		"""
		self.assertFalse(self.harmony.game_solved())

	def testLogic_game_solved(self):
		"""
		testLogic_game_solved
			tests whether a solved game is reported as solved
		"""
		n = 2
		colors = [0,0,1,1]
		swaps = [0,0,0,0]
		harmony = Harmony(n, colors, swaps)

		self.assertTrue(harmony.game_solved())

	################################
	# Testing swaps / unswaps
	################################
	def testSwap_swap(self):
		"""
		testSwap_swap
			tests whether swap correctly swaps two colors,
			decreases the swaps available for each, and decreases
			the total number of swaps left
		"""
		index1 = (0, 1)
		index2 = (1, 1)

		color1, swaps1 = self.harmony.get_by_pair(index1)
		color2, swaps2 = self.harmony.get_by_pair(index2)
		old_total = self.harmony.swaps_left

		# swap here, and then observe new color / swaps
		self.harmony.swap(index1, index2)

		color1_new, swaps1_new = self.harmony.get_by_pair(index1)
		color2_new, swaps2_new = self.harmony.get_by_pair(index2)
		new_total = self.harmony.swaps_left

		# check color swapping
		self.assertEqual(color1, color2_new)
		self.assertEqual(color2, color1_new)

		# check swaps decrease
		self.assertEqual(swaps1_new, swaps1 - 1)
		self.assertEqual(swaps2_new, swaps2 - 1)
		
		# check total swaps decrease
		self.assertEqual(new_total, old_total - 2)

	def testSwap_unswap(self):
		"""
		testSwap_unswap
			tests whether unswap correctly reverts two colors,
			re-increases the swaps available, and re-increases
			the total number of swaps left
		"""
		index1 = (0, 1)
		index2 = (1, 1)

		color1, swaps1 = self.harmony.get_by_pair(index1)
		color2, swaps2 = self.harmony.get_by_pair(index2)
		old_total = self.harmony.swaps_left

		# swap here, and then observe new color / swaps
		self.harmony.unswap(index1, index2)

		color1_new, swaps1_new = self.harmony.get_by_pair(index1)
		color2_new, swaps2_new = self.harmony.get_by_pair(index2)
		new_total = self.harmony.swaps_left

		# check color swapping
		self.assertEqual(color1, color2_new)
		self.assertEqual(color2, color1_new)

		# check swaps decrease
		self.assertEqual(swaps1_new, swaps1 + 1)
		self.assertEqual(swaps2_new, swaps2 + 1)
		
		# check total swaps decrease
		self.assertEqual(new_total, old_total + 2)


if __name__ == '__main__':
	unittest.main()