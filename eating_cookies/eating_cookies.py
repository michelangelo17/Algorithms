#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

# dictionary works because when function first called,
# points to same slot in memory from then on,
# and dictionary is mutable, allowing storage to be passed on


def eating_cookies(n, cache={}):
    # track number of permutations
    count = 0
    # check if n result is in dictionary
    if n in cache:
        return cache[n]
    # if n is less than zero return 0
    # count will remain the same on recursive calls
    if n < 0:
        return 0
    # each zero case is 1 combination
    if n == 0:
        return 1
    # run each n through each possiblity recursively
    # ex: 3 - 3 count 1, 3 - 2, -> 1 - 1, count 2, 3 - 1, 2 -2, count 3 etc.
    # negative values return 0 as above
    count += eating_cookies(n - 3)
    count += eating_cookies(n - 2)
    count += eating_cookies(n - 1)
    # store each number's count in dictionary
    cache[n] = count
    return count


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
