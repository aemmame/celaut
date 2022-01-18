#!/usr/bin/env python
from time import sleep
import argparse
from random import random

character="█"

def d2b(n):
	r=bin(n).replace("0b", "")[-8:]
	return "0"*(8-len(r))+r

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
	all_args.add_argument(type=int, dest="code", default=120, help="Code for cellular automaton")
	all_args.add_argument("-l", "--length", required=False, default=100, dest="length", type=int, help="Length of the board")
	all_args.add_argument("-i","--interval", required=False, default=0.1, dest="interval", type=float, help="Interval between frames (in seconds)")
	all_args.add_argument("-I","--iterations", required=False, default=50, dest="iterations", type=int, help="Total amount of iterations")
	all_args.add_argument("-c","--character", required=False,default=character,dest="character",type=str,help="Character to use as an \"on\" pixel")
	args=all_args.parse_args()
	if not 0<=args.code<=255:
		print("error: code must be in between 0 and 255")
		exit(1)
	if len(args.character)!=1:
		print("error: can only have 1 character as an \"on\" pixel")
		exit(1)
	character=args.character
	board="".join(
		[(character if random() > 0.5 else " ") for _ in range(args.length)]
	)
	for iteration in range(args.iterations):
		print(board)
		board=ca_step(board,args.code)
		sleep(args.interval)

if __name__=="__main__":
	main()
