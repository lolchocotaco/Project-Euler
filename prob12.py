#Problem 12
#What is the value of the first triangle number to have over five hundred divisors?

#Counts numbers of factors for number n
def numFactors(n):
    a = [(i,n/i) for i in range(1,int(n**0.5)+1) if n%i ==0]
    return sum(len(s) for s in a)

#Generator For triangular numbers
def nums():
    triangNum = 1
    natNum = 1
    while 1:
        yield triangNum
        natNum+=1
        triangNum +=natNum;

triGen = nums()         
triangNum = 1;
while(numFactors(triangNum)<500):
    triangNum = next(triGen)
    
    
print("Highly divisible triangular number: {0}".format(triangNum))