#!/usr/bin/python

import sys

## 1. find biggest solution that works
## 2. rotate solution to the right until you get back to original solution
## 3. find next biggest solution, repeat

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cache=None):

  # if cache is null, initialize it
  if cache is None or type(cache) == list:
    cache = {0:1, 1:1, 2:2, 3:4}

  # if answer is in the cache, return answer
  if n in cache.keys():
    return cache[n]
  
  # initialize ways
  ways = 0

  # add eating_cookies(n-i) for i in range 1 to 3 as long
  # as n-i is greater than 0
  for i in range(3):
    if (i+1)>0:
      ways+=eating_cookies(n-(i+1), cache)

  # caching answer
  cache[n] = ways

  return ways

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')