import sys

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

Author
	Menghua Wu
Version
	May 20, 2016
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

		# maintain swaps_left for O(1) checking ending
		# condition; else, need O(n^2) each time
		self.swaps_left = sum(swaps)

		# grid initialization
		for i in range(n):
			self.grid.append([])
			self.grid[i] = row

			for j in range(n):
				index = grid_to_list_index(i, j)
				block = (color[index], swaps[index])

				row.append(block)

		# get starting points, where swaps > 0 
		self.starting_points = []
		for i in range(len(swaps)):
			swap = swaps[i]
			if swap > 0:
				index = list_to_grid_index(i)
				self.starting_points.append(index)

	def usage(self, state):
		"""
		usage
			prompts the user if they have given an
			illegal game configuration

		Parameters
			state: integer of [0, 1, 2]
				0 represents wrong list sizes

				1 represents wrong swaps, e.g. uneven

				2 represents wrong color configuration,
				e.g. not the same number of each color.
		"""
		if state == 0:
			print "Wrong list size for color or swaps."
		elif state == 1:
			print "Uneven number of swaps."
		else:
			print "Not the same number of blocks per color."
		sys.exit(1)

	def get(self, index):
		"""
		get
			returns the tuple stored at grid[i][j],
			where (i, j) is the tuple equivalent of 
			the given index

		Parameters
			index: single integer index representing some
				(i, j) in a one-dimensional form from left
				to right, top to bottom

		Return
			grid[i][j]: if the index is valid
		"""
		try:
			i, j = self.list_to_grid_index(index)
			return grid[i][j]
		except:
			raise KeyError("Invalid grid index.")

	def set(self, index, item):
		"""
		set
			sets the value at grid[i][j] to item, where
			(i, j) is the tuple equivalent of the given index

		Parameters
			index: single integer index representing some
				(i, j) in a one-dimensional form from left
				to right, top to bottom
			item: tuple (color, swap) representing the new 
				value of the block at (i, j)

		Return
			grid[i][j]: if the index is valid
		"""
		try:
			i, j = grid.list_to_grid_index(index)
			self.grid[i][j] = item
			return item
		except:
			raise KeyError("Invalid grid index.")

	def list_to_grid_index(self, index):
		"""
		list_to_grid_index returns the (i, j) tuple form
			of the given index

		Parameters
			index: one-dimensional representation of an
				index (i, j) in grid

		Return
			two-dimensional (i, j) representation of index
		"""
		if not self.valid_index(index):
			raise KeyError("Invalid grid index.")

		# integer division
		return (index / self.n, index % self.n)

	def grid_to_list_index(self, i, j):
		"""
		grid_to_list_index returns the one-dimensional
			index of (i, j) for the given grid of size n

		Parameters
			i: x-value of index
			j: y-value of index

		Return
			one-dimensional representation of (i, j)
		"""
		if not self.valid_index((i, j)):
			raise KeyError("Invalid grid index.")

		return i + self.n * j

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
		# cannot swap with itself
		if index1 == index2:
			return False

		if indices_in_line(index1, index2):
			swap1 = self.get(index1)[1]
			swap2 = self.get(index2)[1]

			return (swap1 > 0 and swap2 > 0)

		# else indices not in line
		return False

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
		return self.swaps_left == 0

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
		# must use all swaps
		if self.has_swaps_left():
			return False

		for i in range(self.n):
			for j in range(self.n):
				if self.grid[i][j] != i:
					return False

		# no swaps left, all colors in orderg
		return True

	################################
	# Pathfinding helper functions
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
		i, j = index

		horizontal = [(i, x) for y in range(self.n)]
		vertical = [(x, j) for x in range(self.n)]

		# overlap of index itself is okay since valid_swap
		# catches not swapping with itself
		possible_moves = horizontal + vertical
		valid_moves = []

		# try them all, in the horizontal and vertical lines
		for move in possible_moves:
			if self.valid_swap(index, move):
				valid_moves.append(move)

		return valid_moves

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

		Return
			True: if successful
			False: otherwise
		"""
		if valid_swap(index1, index2):
			color1, swap1 = self.get(index1)
			color2, swap2 = self.get(index2)

			self.set(index1, (color2, swap1 - 1))
			self.set(index2, (color1, swap2 - 1))

			self.swaps_left -= 2

			return True
		return False

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

		Return
			True: if successful
			False: otherwise
		"""
		if valid_swap(index1, index2):
			color1, swap1 = self.get(index1)
			color2, swap2 = self.get(index2)

			self.set(index1, (color2, swap1 + 1))
			self.set(index2, (color1, swap2 + 1))

			self.swaps_left += 2

			return True
		return False

	################################
	# Main pathfinding algorithm
	################################
	def solve(self):
		"""
		solve
			locates an optimal series of swaps to win the
			game, if possible. It returns that series as
			a list of tuples (index1, index2) of swaps.
			It uses the principles of BFS.

			It tries to start from each block once. each
			iteration, it swaps two blocks to see what happens,
			and if the situation does not lead to a winning
			combination, unswaps and resets the two blocks.

		Return
			[(i1, i2), (j1, j2), ...]: if there exists a
				valid series of swaps to win the game
			None: otherwise
		"""
		for start in self.starting_points:
			pass

