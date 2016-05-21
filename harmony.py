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
		Constructor initializes grid, which is
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
		valid_index returns whether the given index
			is within the bounds of the grid

		Parameters
			index: (i, j) tuple representing the
				index of item grid[i][j]

		Return
			True	if 0 <= i, j < n
			False	otherwise
		"""
		i, j = index
		return (0 <= i < self.n and 0 <= j < self.n)

	def indices_in_line(self, index1, index2):
		"""
		indices_in_line returns whether the items at
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
			True	if i1 == i2 or j1 == j2 and
					both index1 and index2 are valid
			False	otherwise
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

	def valid_swaps(self, index):
		"""
		valid_swaps 

		Parameters
			index: (i, j) tuple representing the
				index of item grid[i][j]
		"""

