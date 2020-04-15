#!/usr/bin/python

import sys


def making_change(amount, denominations):
    # track number of permutations
    count = 0
    # if n is less than zero return 0
    # count will remain the same on recursive calls
    if amount < 0:
        return 0
    # each zero case is 1 combination
    if amount == 0:
        return 1
    # run each n through each possiblity recursively
    # ex: 3 - 3 count 1, 3 - 2, -> 1 - 1, count 2, 3 - 1, 2 -2, count 3 etc.
    # negative values return 0 as above
    for coin in denominations:
        count += making_change(amount - coin, denominations)
    return count


print(making_change(6, [1, 5, 10, 25, 50]))

# if __name__ == "__main__":
#     # Test our your implementation from the command line
#     # with `python making_change.py [amount]` with different amounts
#     if len(sys.argv) > 1:
#         denominations = [1, 5, 10, 25, 50]
#         amount = int(sys.argv[1])
#         print("There are {ways} ways to make {amount} cents.".format(
#             ways=making_change(amount, denominations), amount=amount))
#     else:
#         print("Usage: making_change.py [amount]")
