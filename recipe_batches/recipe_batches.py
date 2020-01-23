#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  
  # initialize min_batches to infinity
  min_batches = float('inf')

  try:
  # loop through all ingredients in recipe and calculate 
  # the number of batches you could make for each
  # while keeping track of the minimum number
    for key in recipe.keys():
      batches = ingredients[key] // recipe[key]
      if batches < min_batches:
        min_batches = batches
  
  except:
    # if there was an error, one of the ingredients in the recipe
    # is not in ingredients
    min_batches = 0

  return min_batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))