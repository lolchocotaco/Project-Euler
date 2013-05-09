# Problem 5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from fractions import gcd

#Calculates Least common multiple of two numbers
def lcm(num1,num2):
    return (num1 * num2) // gcd(num1, num2)
    
#Calculates LCM of multiple numbers
def multiLCM(numbers):
    return reduce(lcm,numbers)

print("Smallest multiple of numbers 1 to 20: %d")%(multiLCM(list((range(1,21)))))
