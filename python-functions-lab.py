#1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(num):
  return sum(range(1, num + 1))
   
print(sum_to(6))



#2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(numbers):
    return max(numbers)

print(largest([3,6,8,9,27]))

#3. Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

def occurrences(phrase, occurrence):
   return phrase.count(occurrence)

print(occurrences("ya mama", "a"))


#4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. (HINT: Review your notes on *args).

import math
def product(*args):
    return math.prod(args)

print(product(2, 3, 6))