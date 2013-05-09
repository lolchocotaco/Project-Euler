# Problem 9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# a^2+b^2+c^2
import operator

triplets =[]
for a in range(1,500):
    for b in range(1,500):
        c = (a**2+b**2)**(0.5)
        if((c%1) == 0): # Its an integer
            triplets.append((a, b, c))

# Using filter with lambda for fun.
# This check could have been done inside the loop
triplet = filter(lambda x: x[0]+x[1]+x[2] ==1000,triplets)
print("Triplet: {0}").format(triplet[1])
print("Product: %d") %(reduce(operator.mul,triplet[1]))