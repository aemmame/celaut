#!/usr/bin/env python
from time import sleep
import argparse
from random import random
import os

VERSION="0.01"

character="█"

# Converts integers into an 8-bit binary number in a string, overflows
def d2b(n):
	r=bin(n).replace("0b", "")[-8:]
	return "0"*(8-len(r))+r

# Performs a 1D CA iteration on a string (I know it's a mess but at least it works, ok)
def ca_step(board,code):
	new_board=""
	code=d2b(code)[::-1]
	for x,pixel in enumerate(board):
		state=[board[(x-1)%len(board)]==character,board[x]==character,board[(x+1)%len(board)]==character]
		for i,case in enumerate(code):
			casestate=[(True if c=="1" else False) for c in d2b(i)[::-1][:3]]
			if casestate==state:
				new_board+=(character if code[i]=="1" else " ")
				break
	return new_board

def main():
	global character
	all_args=argparse.ArgumentParser(prog='celaut')
	all_args.add_argument("-v","--version", action="version", version="celaut "+VERSION, help="Display version and quit")
	all_args.add_argument(type=int, dest="code", default=120, help="Code of the cellular automaton")
	all_args.add_argument("-W", "--width", required=False, default=None, dest="width", type=int, help="Width of the result")
	all_args.add_argument("-H","--height", required=False, default=None, dest="height", type=int, help="Height of the result")
	all_args.add_argument("-i","--interval", required=False, default=0.1, dest="interval", type=float, help="Interval between frames (in seconds)")
	all_args.add_argument("-c","--character", required=False,default=character,dest="character",type=str,help="Character to use as an \"on\" pixel")
	args=all_args.parse_args()
	if not 0<=args.code<=255:
		print("error: code must be in between 0 and 255")
		exit(1)
	if len(args.character)!=1:
		print("error: can only have 1 character as an \"on\" pixel")
		exit(1)
	try:
		terminal_dimensions=os.get_terminal_size()
	except PermissionError:
		if args.width==None or args.height==None:
			print("error: can't figure out the terminal dimensions, specify them in the command")
			exit(1)
	if args.width==None:  args.width=terminal_dimensions[0]
	if args.height==None: args.height=terminal_dimensions[1]-1
	character=args.character
	board="".join(
		[(character if random() > 0.5 else " ") for _ in range(args.width)]
	)
	for iteration in range(args.height):
		print(board)
		board=ca_step(board,args.code)
		sleep(args.interval)

if __name__=="__main__":
	main()


