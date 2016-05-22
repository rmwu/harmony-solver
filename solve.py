import sys
import os
import json
from harmony import Harmony

"""
solve.py is the CLI for solving a game of
Harmony 3, as described in harmony.py

Usage
	solve.py data_filename.txt

Formatting of data_filename.txt
	n
	[color_1, color_2, ... color_n^2]
	[swap_1, swap_2, ... swap_n^2]

Author
	Menghua Wu
Version
	May 21, 2016
"""

args = sys.argv

def usage():
	"""
	usage
		instructs the user about how the use the
		CLI, if invalid options are provided

	Precondition
		User has provided an invalid input, whether
		ommiting the data file or providing a wrong
		filename.

	Postcondition
		Error message has printed. System has quit.
	"""
	print("Usage: %s data_filename.txt" % sys.argv[0])
	sys.exit(1)

def get_harmony_text(filename):
	"""
	get_harmony_text
		loads a harmony data input file and returns
		a dict of its contents, if they are validly
		formatted

	Precondition
		filename contains a validly formatted txt,
		such that the first line contains n, the
		second line contains a list colors, and
		the third line contains a list swaps

	Return
		{
			n: integer,
			colors: list of length n^2, containing
				integers i | 0 <= i < n
			swaps: list of length n^2, containing
				integers i | i >= 0
		}
	"""
	# todo: read in file
	with open(filename, "r") as f:
		data = {}
		try:
			data = json.loads(
			f.read().replace("\'",'"').replace("(", '['
			).replace(")", ']'))

			return data
		except:
			print "Invalid data file formatting."
			usage()

################################
# Run CLI with given data file
################################
if __name__ == "__main__":
	# check for invalid usage
	if len(sys.argv) != 2 or \
		not os.path.exists(sys.argv[1]):
			usage()

	# load data from text file
	data = get_harmony_text(sys.argv[1])

	# get values from data dict
	n = data["n"]
	colors = data["colors"]
	swaps = data["swaps"]

	# load and solve game
	harmony = Harmony(n, colors, swaps)
	path = harmony.solve()

	# print answer
	if path is None:
		print "Sorry! This game has no solution."
	else:
		print "We found a solution!"
		for swap in path:
			print "Swap {} and {}.".format(swap[0], swap[1])