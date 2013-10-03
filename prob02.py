# Project 2
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

fibMax = 4000000

# Fibonacci generator function
# Calculates Fib numbers indefinitely
def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

fibSeq = fib()
fibNum = 0
fibSum = 0  
#Generate Fib numbers and sum them if even.
while fibNum< fibMax:
    fibNum = next(fibSeq)
    if(fibNum%2 == 0):
        fibSum +=fibNum

print ("Sum of even Fibonacci Numbers: %d" %(fibSum))
