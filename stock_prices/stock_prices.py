#!/usr/bin/python

import argparse

def find_max_profit(prices):

  # Check that there are at least 2 prices
  if len(prices) < 2:
    raise Exception('Price array does not contain 2 or more prices')

  # initialize max profit
  max_profit = prices[1] - prices[0]

  for i, price_1 in enumerate(prices):
    for price_2 in prices[i+1:]:
      profit = price_2 - price_1
      if profit > max_profit:
        max_profit = profit

  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))