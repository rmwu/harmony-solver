import sys
import copy

"""
Harmony 3 is an iOS game that prompts the user to
reproduce a certain configuration of color blocks,
given an exact number of required swaps per block,
between blocks directly inline with each other,
horizontally and vertically.

For more information, visit:
https://itunes.apple.com/us/app/har-mo-ny-3/id982805507?mt=8

This is a DFS solver for Harmony 3. This project
is not intended to infringe upon any copyright.
Rather, it is a good natured programming exercise.

Author
	Menghua Wu
Version
	May 23, 2016
"""
debug = True

class Harmony():
	"""
	Harmony represents the grid of the game, which
	is an n by n square. The grid is indexed (0,0)
	at the top-left corner.

	Instance Variables
		n: side length of game
		colors: length n^2 list of colors, representing a 
			grid going from top left to bottom right. The
			value of colors is 0 <= color < n.
		swaps: length n^2 list of swap counts, representing
			a grid going from top left to bottom right. The
			number of swaps is s >= 0.

		list_to_grid: dictionary mapping one-dimensional list
			indices to their equivalent (i, j) tuple form
		grid_to_list: dictionary mapping (i, j) tuples to
			their equivalent list index forms

		swaps_left: number of total swaps remaining among
			all blocks in grid.
		swapping_points: dict keyed by list integer indices
			that, at the any point in the game, follow the
			property that swaps[index] has > 0 swaps. Used for 
			O(1) deletion and insertion.
		one_swap_points: dict keyed by list integer indices
			that, at the any point in the game, follow the
			property that swaps[index] = 1. Used for trivial
			swapping cases to reduce search space.
	"""

	################################
	# Constructor, index arithmetic
	################################

	def __init__(self, n = 0, colors = None, swaps = None):
		"""
		Constructor
			initializes n, colors, and swaps as provided.
			Determines swaps_left and creates a list of
			swapping_points from which to begin the search

		Parameters
			n: side length of game
			colors: specifies color in each block,
				from left to right, top to bottom.
				For this game, 0 < color < n.
			swaps: specifies the number of swaps
				required for each block, from left
				to right, top to bottom. For this game,
				number of swaps >= 0
		"""		
		# if one is not provided, then we cannot have
		# a valid game
		if not colors or not swaps:
			self.usage(0)

		if len(colors) != n**2 or len(swaps) != n**2:
			self.usage(1)

		self.n = n

		# maintain swaps_left for O(1) checking search over
		self.swaps_left = sum(swaps)

		self.colors = colors
		self.swaps = swaps

		# index manipulation initialization
		self.list_to_grid = {}
		self.grid_to_list = {}

		l2g = self.list_to_grid # faster calls
		g2l = self.grid_to_list

		for i in range(n):
			for j in range(n):
				grid_ind = (i, j)
				list_ind = i*n + j
				
				l2g[list_ind] = grid_ind
				g2l[grid_ind] = list_ind

		# get one swap points for faster end condition
		# get starting points, where swaps > 0
		# other valid points, if not here, will be added
		# as the algorithm runs
		self.one_swap_points = {}
		self.swapping_points = {}
		for i in range(n**2):
			swap = swaps[i]
			if swap > 0: # can start from this point
				self.swapping_points[i] = True
				if swap == 1: # deterministic swaps
					self.one_swap_points[i] = True

		# for faster checking of valid swaps
		# stored in list index format
		self.adjacent_points = {}
		for i in range(n):
			for j in range(n):
				horizontal = [g2l[(i, y)] for y in range(n)]
				vertical = [g2l[(x, j)] for x in range(n)]
				self.adjacent_points[g2l[(i, j)]] = horizontal + vertical

	def usage(self, state):
		"""
		usage
			prompts the user if they have given an
			illegal game configuration

		Parameters
			state: integer of [0, 1, 2]
				0 represents absence of data

				1 represents wrong data size

				2 represents wrong color configuration,
				e.g. not the same number of each color.
		"""
		print "Your input file is improperly formatted."

		if state == 0:
			print "Please provide colors and/or swaps"
		elif state == 1:
			print "Wrong list size for color or swaps."
		else: # currently unused, may implement in future
			print "Not the same number of blocks per color."
		sys.exit(1)

	def get(self, index):
		"""
		get
			returns the tuple (color, swaps) stored at index,
			which is an integer list index

		Parameters
			index: single integer index representing some
				(i, j) in a one-dimensional form from left
				to right, top to bottom

		Return
			(colors[index], swaps[index]): if index valid
		"""
		return (self.get_color(index), self.get_swaps(index))

	def get_color(self, index):
		"""
		get_color
			returns the color stored at colors[index]

		Parameters
			index: single integer index representing some
				(i, j) in a one-dimensional form from left
				to right, top to bottom

		Return
			colors[index]: if the index is valid
		"""
		try:
			return self.colors[index]
		except:
			raise KeyError("Invalid list index {}.".format(index))

	def get_swaps(self, index):
		"""
		get_swaps
			returns the color stored at swaps[index]

		Parameters
			index: single integer index representing some
				(i, j) in a one-dimensional form from left
				to right, top to bottom

		Return
			swaps[index]: if the index is valid
		"""
		try:
			return self.swaps[index]
		except:
			raise KeyError("Invalid list index {}.".format(index))

	# deprecated
	def get_by_pair(self, pair):
		"""
		get_by_pair
			returns the tuple stored at grid[i][j],
			where pair = (i, j)

		Parameters
			index: (i, j) tuple representing the
				index of item grid[i][j]

		Return
			grid[i][j]: if the index is valid
		"""
		try:
			i, j = pair
			return self.grid[i][j]
		except:
			raise KeyError("Invalid grid index {}.".format(pair))

	def set_value(self, index, color, swaps):
		"""
		set_value
			sets the value at grid[i][j] to item, where
			(i, j) is the tuple equivalent of the given index

		Parameters
			index: integer list index representing some
				(i, j) in a one-dimensional form from left
				to right, top to bottom
			color: integer 0 <= color < n
			swaps: integer swaps >= 0

		Return
			(color, swaps): if the index is valid
		"""
		try:
			self.colors[index] = color
			self.swaps[index] = swaps
			return (color, swaps)
		except:
			raise KeyError("Invalid grid index {}.".format(index))

	# deprecated
	def set_value_by_pair(self, pair, item):
		"""
		set_value_by_pair
			sets the value at grid[i][j] to item, where
			pair = (i, j)

		Parameters
			pair: (i, j) tuple representing the index of
				item grid[i][j]
			item: tuple (color, swap) representing the new 
				value of the block at (i, j)

		Return
			grid[i][j]: if the index is valid
		"""
		try:
			i, j = pair
			self.grid[i][j] = item
			return item
		except:
			raise KeyError("Invalid grid index {}.".format(pair))

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
		# integer division
		return self.list_to_grid[index]
		# return (index / self.n, index % self.n)

	def grid_to_list_index(self, index):
		"""
		grid_to_list_index returns the one-dimensional
			index of (i, j) for the given grid of size n

		Parameters
			index: tuple (i, j) of integers

		Return
			one-dimensional representation of (i, j)
		"""
		return self.grid_to_list[index]
		# return i * self.n + j

	def valid_index(self, index):
		"""
		valid_index
			returns whether the given index
			is within the bounds of the grid

		Parameters
			index: integer list index

		Return
			True: if 0 <= index < n^2
			False: otherwise
		"""
		return (0 <= index < self.n**2)

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
			index1: list integer index
			index2: list integer index

		Return
			True: if grid forms of index1 and index2
				are in line with each other
			False: otherwise
		"""
		# check if index1 and index2 are valid
		# uncomment for slower, safer code
		"""
		for index in [index1, index2]:
			if not self.valid_index(index):
				return False
		"""
		# now check if index1 and index2 are colinear
		i1, j1 = self.list_to_grid[index1]
		i2, j2 = self.list_to_grid[index2]

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
			index1: list integer index
			index2: list integer index

		Return
			True: if index1, index2 are colinear
				and the blocks at these locations
				both have > 0 swaps available
			False: otherwise
		"""
		# cannot swap with itself
		if index1 == index2:
			return False

		if self.indices_in_line(index1, index2):
			color1, swap1 = self.get(index1)
			color2, swap2 = self.get(index2)

			# don't allow impossible situations
			# if swap to a row that is impossible
			if ((swap1 < 2 and 
			    color1 != self.list_to_grid[index2][0]) or
				(swap2 < 2 and 
				color2 != self.list_to_grid[index1][0])):
				return False

			return (swap1 > 0 and swap2 > 0)

		# else indices not in line
		return False

	def has_swaps_left(self):
		"""
		has_swaps_left
			returns whether or not there are enough swaps
			left to finish the game

		Return
			True: if the number of swaps left greater than 0
			False: otherwise
		"""
		return self.swaps_left > 0

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
				index = self.grid_to_list[(i, j)]
				# check row number only
				if self.colors[index] != i:
					return False

		# no swaps left, all colors in order
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
			index: list integer index

		Return
			[index1, index2, ...] of valid swaps starting
			from the given index
		"""
		# overlap of index itself is okay since valid_swap
		# catches not swapping with itself
		possible_moves = self.adjacent_points[index]
 		valid_moves = []

		# try them all, in the horizontal and vertical lines
		for move in possible_moves:
			if self.valid_swap(index, move):
				valid_moves.append(move)

		return valid_moves

	def get_one_swappable(self):
		"""
		get_swappable
			finds and returns a list of indices containing
			swappable blocks, with swaps = 0

		Return
			[index1, index2, ...] of valid one-swap blocks
			remaining
		"""
		one_swap = self.one_swap_points
		return [ind for ind in one_swap
				if one_swap[ind]]

	def get_swappable(self):
		"""
		get_swappable
			finds and returns a list of indices containing
			swappable blocks, with swaps > 0

		Return
			[index1, index2, ...] of valid swappable blocks
			remaining
		"""
		swapping_points = self.swapping_points
		return [ind for ind in swapping_points
				if swapping_points[ind]]

	def swap(self, index1, index2):
		"""
		swap
			swaps the colors at index1, index2, if the
			action is valid as defined by valid_swap,
			and decreases the swap count accordingly

		Parameters
			index1: list integer index
			index2: list integer index

		Postcondition
			The colors at index1, index2 are swapped.
			The total swap count has been decreased by 2,
			and the individual swap counts of index1, index2
			have each decreased by 1.

		Return
			True: if successful
			False: otherwise
		"""
		if self.valid_swap(index1, index2):
			color1, swap1 = self.get(index1)
			color2, swap2 = self.get(index2)

			self.set_value(index1, color2, swap2 - 1)
			self.set_value(index2, color1, swap1 - 1)

			# check if no longer swappable
			swapping_points = self.swapping_points
			one_swap = self.one_swap_points

			if swap2 < 2:
				swapping_points[index1] = False
				one_swap[index1] = False
			if swap1 < 2:
				swapping_points[index2] = False
				one_swap[index2] = False

			if swap2 == 3:
				one_swap[index1] = True
			if swap1 == 3:
				one_swap[index2] = True

			self.swaps_left -= 2

			return True
		return False

	def unswap(self, index1, index2):
		"""
		unswap
			resets the colors at index1, index2 to what
			they were before swap(index1, index2) was
			called. Swap counts are increased accordingly.

		Parameters
			index1: list integer index
			index2: list integer index

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
		color1, swap1 = self.get(index1)
		color2, swap2 = self.get(index2)

		self.set_value(index1, color2, swap2 + 1)
		self.set_value(index2, color1, swap1 + 1)

		# reinstate swap availability, if needed
		swapping_points = self.swapping_points
		swapping_points[index1] = True
		swapping_points[index2] = True

		one_swap = self.one_swap_points
		if swap2 == 0:
			one_swap[index1] = True
		if swap1 == 0:
			one_swap[index2] = True

		self.swaps_left += 2

		return True

	def deterministic_swaps(self, path):
		"""
		deterministic_swaps
			finds swaps that must occur, due to one-swap
			blocks in facing colors. This is meant to reduce
			the search space before beginning, for performance.

		Parameters
			path: list of tuples of indices, detailing swap order

		Return
			path: changed or unchanged

		Postcondition:
			If any swaps of colinear one-swap blocks exist,
			then they have been performed.
		"""
		one_swap = self.get_one_swappable()
		for index1 in one_swap:
			for index2 in one_swap:
				# if they are in line and work for swaps
				if self.valid_swap(index1, index2):
					self.swap(index1, index2)
					path.append((index1, index2))
		return path

	################################
	# Main pathfinding algorithm
	################################
	def solve(self):
		"""
		solve
			locates an optimal series of swaps to win the
			game, if possible. It returns that series as
			a list of tuples (index1, index2) of swaps.
			It uses the principles of DFS.

			It tries to start from each block once. each
			iteration, it swaps two blocks to see what happens,
			and if the situation does not lead to a winning
			combination, unswaps and resets the two blocks.

		Return
			[(index1, index2), ...]: if there exists a
				valid series of swaps to win the game
			None: otherwise
		"""
		if self.game_solved():
			return []

		starting_points = self.swapping_points.keys()
		start_path = self.deterministic_swaps([])

		for start in starting_points:
			if debug:
				print "Starting at {}\n".format(start)

			start_copy = [swap for swap in start_path]
			path = self.find_path(start, start_copy, set())

			if path is not None:
				return self.format_path(path)

		return None

	def find_path(self, index1, path = [], tried = set()):
		"""
		find_path
			is a recursive helper function for solve. It tries
			to DFS from all different paths

		Parameters
			index: list integer index

		Return
			[(index1, index2), ...]: if there exists a
				valid series of swaps to win the game
			[]:	if no swaps are needed; the game is done
			None: otherwise
		"""
		#if debug:
		#	print "Index1: {}".format(index1)
		
		# base case, no more swaps
		if not self.has_swaps_left():
			if self.game_solved():
				return path
			return None

		# reduce search space
		# path = self.deterministic_swaps(path)

		swappable = self.valid_moves(index1)

		# explore each path
		for index2 in swappable:
			swap_pair = (index1, index2)
			path.append(swap_pair)

			# tuples are hashable
			path_tup = tuple(path)
			if path_tup not in tried:
				tried.add(path_tup)

				# try to swap it and see what happens
				self.swap(index1, index2)

				if self.game_solved():
					return path

				# now try all remaining possibilities
				remaining = self.get_swappable()

				for index3 in remaining:
					new_path = self.find_path(index3, path, tried)

					if new_path:
						return new_path

			# if no path, undo the swapping
			path.pop()
			self.unswap(index1, index2)
		
		return None

	def format_path(self, path):
		"""
		format_path
			translates the path into a human-readable
			format by turning the list indices into
			1-indexed grid index strings

		Return
			[("Row x1, Col y1", "Row x2, Col y2"), ...]
		"""
		human_readable_path = []
		for pair in path:
			x1, y1 = self.list_to_grid_index(pair[0])
			x2, y2 = self.list_to_grid_index(pair[1])

			index1 = "Row {}, Col {}".format(x1 + 1, y1 + 1)
			index2 = "Row {}, Col {}".format(x2 + 1, y2 + 1)

			human_readable_path.append((index1, index2))

		return human_readable_path