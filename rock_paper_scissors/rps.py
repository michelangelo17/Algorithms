#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # create nested lists times amount
    # ex: n = 2 results -> [['rock', 'paper', 'scissors'], ['rock', 'paper', 'scissors']]
    moves_lists = [['rock', 'paper', 'scissors']] * n
    result = [[]]
    # for each array in nested moves array
    for moves in moves_lists:
        # list comprehension to split list using nested for loop and combine on left
        # result for y first pass creates 'rock', 'paper' 'scissors'
        # x for first pass creates []
        # [] + ['rock'] = [['rock]]
        # then result for second pass is [['rock], ['paper], ['scissors']]
        # x = ['rock'] + [y='rock'] giving us [['rock', 'rock']]
        result = [x+[y] for x in result for y in moves]
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
