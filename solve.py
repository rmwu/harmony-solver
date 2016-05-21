import sys
import os
from harmony import *

"""
solve.py is the CLI for solving a game of
Harmony 3, as described in harmony.py
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
	with open filename as f:
		pass

if __name__ == "__main__":
	if len(sys.argv) != 2 or \
		not os.path.exists(sys.argv[1]):
			usage()

	data = get_harmony_text(sys.argv[1])

	# todo: implement solving