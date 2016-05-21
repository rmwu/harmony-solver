"""
Harmony 3 is an iOS game that prompts the user to
reproduce a certain configuration of color blocks,
given an exact number of required swaps per block,
between blocks directly inline with each other,
horizontally and vertically.

For more information, visit .

This is a BFS solver for Harmony 3. This project
is not intended to infringe upon any copyright.
Rather, it is a good natured programming exercise.

Author: Menghua Wu
Version: May 20, 2016
"""

class Harmony():
	"""
	Harmony represents the grid of the game, which
	is an n by n square. The grid is indexed (0,0)
	at the top-left corner.
	"""

	################################
	# Constructor, index arithmetic
	################################

	def __init__(self, n = 0, colors = None, swaps = None):
		"""
		Constructor
			initializes grid, which is
			represented as a two-dimensional array.
			Colors and swaps for each block are 
			represented in a tuple of form (color, swap).

		Parameters
			n: side length of game
			colors: specifies color in each block,
				from left to right, top to bottom.
				For this game, 0 < color < n.
			swaps: specifies the number of swaps
				required for each block, from left
				to right, top to bottom.
				For this game, number of swaps >= 0
		"""
		# if one is not provided, then we cannot have
		# a valid game
		if not colors or not swaps:
			n = 0

		self.n = n

		# maintain moves_left for O(1) checking ending
		# condition; else, need O(n^2) each time
		self.moves_left = sum(swaps)

		# todo: initialize grid here
		self.grid = []

		for i in range(n):
			self.grid.append([])
			self.grid[i] = row

			for j in range(n):
				index = grid_to_list_index(i, j)
				block = (color[index], swaps[index])

				row.append(block)

	def list_to_grid_index(self, i):
		"""
		"""
		pass

	def grid_to_list_index(self, i, j):
		"""
		"""
		pass

	def valid_index(self, index):
		"""
		valid_index
			returns whether the given index
			is within the bounds of the grid

		Parameters
			index: (i, j) tuple representing the
				index of item grid[i][j]

		Return
			True: if 0 <= i, j < n
			False: otherwise
		"""
		i, j = index
		return (0 <= i < self.n and 0 <= j < self.n)

	def indices_in_line(self, index1, index2):
		"""
		indices_in_line
			returns whether the items at
			index1 and index2 can be legally swapped
			in this grid. Legal swaps are allowed
			between blocks directly inline with each
			other, horizontally or vertically.

		Note
			indices_in_line does not check whether the
			items have swaps available, or if it will
			produce a more optimal setup. It only checks
			the grid for valid colinearity.

		Parameters
			index1: (i1, j1) tuple representing
				the index of item grid[i1][j1]
			index2: (i2, j2) tuple representing
				the index of item grid[i2][j2]

		Return
			True: if i1 == i2 or j1 == j2 and
				both index1 and index2 are valid
			False: otherwise
		"""
		# check if index1 and index2 are valid
		for index in [index1, index2]:
			if not self.valid_index(index):
				return False

		# now check if index1 and index2 are colinear
		i1, j1 = index1
		i2, j2 = index2

		return (i1 == i2 or j1 == j2)

	################################
	# Basic logic rules for the game
	################################
	def valid_swap(self, index1, index2):
		"""
		valid_swaps
			returns whether or not a swap is valid
			in this game, given the number of swaps
			available

		Parameters
			index1: (i1, j1) tuple representing
				the index of item grid[i1][j1]
			index2: (i2, j2) tuple representing
				the index of item grid[i2][j2]

		Return
			True: if index1, index2 are colinear
				and the blocks at these locations
				both have > 0 swaps available
			False: otherwise
		"""
		pass

	def has_swaps_left(self):
		"""
		has_swaps_left
			returns whether or not there are enough swaps
			left to finish the game

		Return
			True: if the number of swaps left is an even
				number > 0
			False: otherwise
		"""
		pass

	def game_solved(self):
		"""
		game_solved
			returns whether or not the game of Harmony
			has been solved. If the game is solved, there
			are no remaining swaps left, and the colors
			are ordered in the gradient, with color 0 at
			the top and color n-1 at the bottom.

		Return
			True: if all swaps are 0, and the blocks are
				in order of color by row
			False: otherwise
		"""
		pass

	################################
	# Pathfinding functionality
	################################
	def valid_moves(self, index):
		"""
		valid_moves
			returns a list of valid swapping candidates
			from the given index. These indices must be
			valid swaps, as defined by valid_swap.

		Parameters
			index: (i, j) tuple representing the
				index of item grid[i][j]

		Return
			[index1, index2, ...] of valid swaps starting
			from the given index
		"""
		pass

	def swap(self, index1, index2):
		"""
		swap
			swaps the colors at index1, index2, if the
			action is valid as defined by valid_swap,
			and decreases the swap count accordingly

		Postcondition
			The colors at index1, index2 are swapped.
			The total swap count has been decreased by 2,
			and the individual swap counts of index1, index2
			have each decreased by 1.
		"""
		pass

	def unswap(self, index1, index2):
		"""
		unswap
			resets the colors at index1, index2 to what
			they were before swap(index1, index2) was
			called. Swap counts are increased accordingly.

		Precondition
			The colors at index1, index2 were swapped in
			some previous iteration, so that this operation
			makes sense

		Postcondition:
			The colors at index1, index2 are swapped.
			The total swap count has been increased by 2,
			and the individual swap counts of index1, index2
			have each increased by 1.
		"""
		pass

