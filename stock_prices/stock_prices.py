#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # copy list in case max is at index 0
    prices_copy = prices[:]

    # find min and max values and index
    min_price = min(prices_copy)
    max_price = max(prices_copy)
    min_index = prices_copy.index(min_price)
    max_index = prices_copy.index(max_price)

    # optimisation in case min and max are arranged ideally
    if min_index < max_index:
        return max_price - min_price

    # remove max from beginning of array to resolve edge case
    # example: 1000, 100, 10 would result in -900 without this
    while max_index == 0 and len(prices_copy) > 2:
        prices_copy.pop(0)
        max_price = max(prices_copy)
        max_index = prices_copy.index(max_price)

    else:
        # set default values to first array pair to handle negative responses
        best_with_max = prices_copy[1] - prices_copy[0]
        best_with_min = prices_copy[1] - prices_copy[0]

        # test with values to the left of max index
        for i in range(1, max_index):
            test_with_max = max_price - prices_copy[i]
            if test_with_max > best_with_max:
                best_with_max = test_with_max

        # test with values to the right of min_index
        for j in range(min_index + 1, len(prices_copy)):
            test_with_min = prices_copy[j] - min_price
            if test_with_min > best_with_min:
                best_with_min = test_with_min

        # return largest value
        if best_with_max > best_with_min:
            return best_with_max
        else:
            return best_with_min


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
