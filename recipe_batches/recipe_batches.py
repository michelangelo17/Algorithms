#!/usr/bin/python

import math

# Assuming recipe and ingredients have same order
# Assuming recipe and ingredient names match
# Tests back both assumuptions.


def recipe_batches(recipe, ingredients):
    # convert values in each dictionary to lists
    recipe_amounts = list(recipe.values())
    ingredients_ammounts = list(ingredients.values())
    # set up the array for result of floor division
    batches_amounts = []
    # if missing any ingredients return zero
    if len(recipe_amounts) > len(ingredients_ammounts):
        return 0
    # for each ingredient amount floor divide by recipe amount
    for i in range(0, len(ingredients_ammounts)):
        batches_amounts.append(ingredients_ammounts[i] // recipe_amounts[i])
    # return smallest value possible
    return min(batches_amounts)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
