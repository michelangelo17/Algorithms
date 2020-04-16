#!/usr/bin/python

import sys
# i know this is 'not advised', but this is a good, fast solution so i'm doing it anyway
sys.setrecursionlimit(10**5)


def making_change(amount, denominations, cache={1: {}, 5: {}, 10: {}, 25: {}, 50: {}}):
    # in below loop, the beginning of the list is changed as it goes through
    # sets current_coin to beginning of that array to use with cache dictionary
    current_coin = denominations[0]
    # checks cache for amount with list beggining with current coin
    if amount in cache[current_coin]:
        return cache[current_coin][amount]
    # holds permutation count
    count = 0
    # base case is to exactly hit one, means coin combination subtracted down evenly
    if amount < 0:
        return 0
    if amount == 0:
        return 1
    # loop over denominations array, checking each coin recursively
    # uses index to prevent repeating coin combinations.
    # ex: 6 -> 1, 5 when current_coin is 1, then when current coin is 5
    # there will be no 1 to combine with, so will not get a reversed 5, 1 double count
    for i, coin in enumerate(denominations):
        count += making_change(amount - coin, denominations[i:])
    # add new amount values for current coin dictionary in cache
    cache[current_coin][amount] = count
    return count


print(making_change(10000, [1, 5, 10, 25, 50]))

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")

# solution without comments:
# import sys
# sys.setrecursionlimit(10**5)

# def making_change(amount, denominations, cache={1: {}, 5: {}, 10: {}, 25: {}, 50: {}}):
#     current_coin = denominations[0]
#     if amount in cache[current_coin]:
#         return cache[current_coin][amount]
#     count = 0
#     if amount < 0:
#         return 0
#     if amount == 0:
#         return 1
#     for i, coin in enumerate(denominations):
#         count += making_change(amount - coin, denominations[i:])
#     cache[current_coin][amount] = count
#     return count
