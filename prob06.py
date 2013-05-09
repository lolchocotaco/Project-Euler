# Problem 6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sumSquare = sum([x*x for x in range(1,101)])
squareSum = sum(range(1,101))**2
print("Difference: %d")%(squareSum- sumSquare)