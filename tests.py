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
	May 23, 2016
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

		self.n = 2
		colors = [0,1,1,0]
		swaps = [0,1,0,1]
		self.harmony = Harmony(self.n, colors, swaps)

	################################
	# Testing Harmony constructor
	################################
	def testConstructor_n(self):
		"""
		testConstructor_n
			tests whether Harmony creates an object
			knowing its correct size
		"""
		self.assertEqual(self.n, self.harmony.n)

	def testConstructor_grid_size(self):
		"""
		testConstructor_grid_size
			tests whether Harmony initializes colors
			and swaps of the right size
		"""
		size = self.n**2
		self.assertEqual(size, len(self.harmony.colors))
		self.assertEqual(size, len(self.harmony.swaps))

	def testConstructor_swaps_left(self):
		"""
		testConstructor_swaps_left
			tests whether Harmony records the correct
			number of swaps available upon creation
		"""
		self.assertEqual(2, self.harmony.swaps_left)

	def testConstructor_swapping_points_none(self):
		"""
		testConstructor_swapping_points_none
			tests that Harmony extracts the correct
			starting points, given that there are none
		"""
		n = 2
		colors = [0,1,1,0]
		swaps = [0,0,0,0]
		harmony = Harmony(n, colors, swaps)

		swapping_points = set()

		self.assertEqual(swapping_points, set(harmony.swapping_points))

	def testConstructor_swapping_points_exist(self):
		"""
		testConstructor_swapping_points_exist
			tests that Harmony extracts the correct
			starting points, given that they exist
		"""
		swapping_points = set([1, 3])

		self.assertEqual(swapping_points, set(self.harmony.swapping_points))

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
						self.harmony.grid_to_list_index(g))

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
						self.harmony.grid_to_list_index(g))

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
		index1 = 0
		index2 = 1

		self.assertTrue(self.harmony.indices_in_line(index1, index2))

	def testIndexManip_indices_in_line_vertical(self):
		"""
		testIndexManip_indices_in_line_vertical tests
			whether two vertical colinear indices are
			reported as in line with each other
		"""
		index1 = 0
		index2 = 2

		self.assertTrue(self.harmony.indices_in_line(index1, index2))

	def testIndexManip_indices_in_line_nonlinear(self):
		"""
		testIndexManip_indices_in_line_nonlinear
			tests whether two non-linear indices are
			reported as in not line with each other
		"""
		index1 = 0
		index2 = 3

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
		old_color, old_swaps = self.harmony.get(index)
		color, swaps = (1, 1)

		# should not be equal before setting
		self.assertNotEqual((color, swaps),
		                    self.harmony.get(index))

		self.harmony.set_value(index, color, swaps)
		
		# should be equal after setting
		self.assertEqual((color, swaps),
		                 self.harmony.get(index))

		# restore the original grid
		self.harmony.set_value(index, old_color, old_swaps)

	################################
	# Testing game logic
	################################
	def testLogic_valid_swap(self):
		"""
		testLogic_valid_swap
			tests whether a valid swap is reported as valid
		"""
		index1 = 1
		index2 = 3

		self.assertTrue(self.harmony.valid_swap(index1, index2))

	def testLogic_invalid_swap(self):
		"""
		testLogic_invalid_swap
			tests whether a invalid swap is reported as 
			not valid
		"""
		index1 = 0
		index2 = 2

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
	# Testing pathfinding helpers
	################################
	def testPathfinding_swap(self):
		"""
		testPathfinding_swap
			tests whether swap correctly swaps two colors,
			decreases the swaps available for each, and decreases
			the total number of swaps left
		"""
		index1 = 1
		index2 = 3

		color1, swaps1 = self.harmony.get(index1)
		color2, swaps2 = self.harmony.get(index2)
		old_total = self.harmony.swaps_left

		# swap here, and then observe new color / swaps
		self.harmony.swap(index1, index2)

		color1_new, swaps1_new = self.harmony.get(index1)
		color2_new, swaps2_new = self.harmony.get(index2)
		new_total = self.harmony.swaps_left

		# check color swapping
		self.assertEqual(color1, color2_new)
		self.assertEqual(color2, color1_new)

		# check swaps decrease
		self.assertEqual(swaps1_new, swaps1 - 1)
		self.assertEqual(swaps2_new, swaps2 - 1)
		
		# check total swaps decrease
		self.assertEqual(new_total, old_total - 2)

	def testPathfinding_unswap(self):
		"""
		testPathfinding_unswap
			tests whether unswap correctly reverts two colors,
			re-increases the swaps available, and re-increases
			the total number of swaps left
		"""
		index1 = 1
		index2 = 3

		color1, swaps1 = self.harmony.get(index1)
		color2, swaps2 = self.harmony.get(index2)
		old_total = self.harmony.swaps_left

		# swap here, and then observe new color / swaps
		self.harmony.unswap(index1, index2)

		color1_new, swaps1_new = self.harmony.get(index1)
		color2_new, swaps2_new = self.harmony.get(index2)
		new_total = self.harmony.swaps_left

		# check color swapping
		self.assertEqual(color1, color2_new)
		self.assertEqual(color2, color1_new)

		# check swaps decrease
		self.assertEqual(swaps1_new, swaps1 + 1)
		self.assertEqual(swaps2_new, swaps2 + 1)
		
		# check total swaps decrease
		self.assertEqual(new_total, old_total + 2)

	def testPathfinding_valid_moves_none(self):
		"""
		testPathfinding_valid_moves_none
			verifies that the valid_moves locates no valid
			moves if there are none
		"""
		index = 0

		self.assertEqual([], self.harmony.valid_moves(index))

	def testPathfinding_valid_moves_one(self):
		"""
		testPathfinding_valid_moves_one
			verifies that the valid_moves locates all valid
			moves, one in this case
		"""
		index = 1

		self.assertEqual([3], self.harmony.valid_moves(index))

	def testPathfinding_valid_moves_many(self):
		"""
		testPathfinding_valid_moves_many
			verifies that the valid_moves locates all valid
			moves, many in this case
		"""
		n = 2
		colors = [1,1,0,0]
		swaps = [1,1,1,1]
		harmony = Harmony(n, colors, swaps)

		index = 0
		valid = [2]

		self.assertEqual(valid, harmony.valid_moves(index))

	def testPathfinding_get_swappable_none(self):
		"""
		testPathfinding_get_swappable_none
			tests that get_swappable returns an empty list
			given no swaps available
		"""
		n = 2
		colors = [0,0,1,1]
		swaps = [0,0,0,0]
		harmony = Harmony(n, colors, swaps)

		self.assertEqual(harmony.get_swappable(), [])

	def testPathfinding_get_swappable_many(self):
		"""
		testPathfinding_get_swappable_many
			tests that get_swappable returns a correct
			list of still swappable states, if there are
			some
		"""
		swappable = set([1,3])

		self.assertEqual(swappable,
		                set(self.harmony.get_swappable()))

	################################
	# Testing search algorithm
	################################
	def testSearch_none(self):
		"""
		testSearch_none
			tests if None is returned upon an impossible situation
		"""
		n = 2
		colors = [1,1,0,0]
		swaps = [0,0,0,0]
		harmony = Harmony(n, colors, swaps)
		path = harmony.solve()

		assert path is None

	def testSearch_complete(self):
		"""
		testSearch_complete
			tests if an empty array is returned upon an already
			solved game
		"""
		n = 2
		colors = [0,0,1,1]
		swaps = [0,0,0,0]
		harmony = Harmony(n, colors, swaps)
		path = harmony.solve()

		self.assertEqual(path, [])

	def testSearch_path_small(self):
		"""
		testSearch_path_small
			tests if a valid path is found, given that it exists
			and the game does not start solved

			This path has length 1.
		"""
		path = self.harmony.solve()
		actual_length = 1

		self.assertEqual(len(path), actual_length)

if __name__ == '__main__':
	unittest.main()