#!/usr/bin/python

import argparse


def find_max_profit(prices):

    # find min and max values and index
    min_price = min(prices)
    max_price = max(prices)
    min_index = prices.index(min_price)
    max_index = prices.index(max_price)
    end_index = len(prices) - 1

    # optimisation in case min and max are arranged ideally
    if min_index < max_index:
        return max_price - min_price
    else:

        # set default values to first and last array pairs
        # this way, negative values handled correctly
        best_with_max = prices[1] - prices[0]
        best_with_min = prices[end_index] - prices[end_index - 1]

        # test with values to the left of max index
        for i in range(1, max_index):
            test_with_max = max_price - prices[i]
            if test_with_max > best_with_max:
                best_with_max = test_with_max

        # test with values to the right of min_index
        for j in range(min_index + 1, end_index - 1):
            test_with_min = prices[j] - min_price
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
