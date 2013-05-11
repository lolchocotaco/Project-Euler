#Problem 14
# Which starting number, under one million, produces the longest sequence
#n  n/2 (n is even)
#n  3n + 1 (n is odd)

def nextNum(n):
    if(n==1):
        break
    elif(n%2 ==0):
        return n/2
    else:
        return 3*n+1

def genChain(n): pass

longestChain = 0
for i in range(1000000):
    chainLength = len(genChain(i))
    if( chainLength> longestChain):
        longestChain =chainLength
