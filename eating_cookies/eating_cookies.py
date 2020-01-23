#!/usr/bin/python

import sys

test {1:1,
      2:2,
      3:4,
      4:7,
      5:13,
}

4

31
13
22
211
121
112
111

## 1. find biggest solution that works
## 2. rotate solution to the right until you get back to original solution
## 3. find next biggest solution, repeat

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  pass

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')