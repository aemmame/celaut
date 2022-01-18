import sys
from time import sleep
import argparse

def main():
	all_args=argparse.ArgumentParser()
	all_args.add_argument(type=int, dest="code", default=120, help="Code for cellular automaton")
	all_args.add_argument("-l", "--length", required=False, default=40, dest="length", type=int, help="Length of the board")
	all_args.add_argument("-i","--interval", required=False, default=0.1, dest="interval", type=float, help="Interval between frames (in seconds)")
	all_args.add_argument("-I","--iterations", required=False, default=50, dest="steps", type=int, help="Total amount of iterations")
	args=all_args.parse_args()
	print(args)
if __name__=="__main__":
	main()
