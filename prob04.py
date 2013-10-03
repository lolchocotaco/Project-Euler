# Problem 4
# Find the largest palindrome made from the product of two 3-digit numbers.

maxNum = 998001
startNum, stopNum = 100, 999

product = 0
strProd = ""
pDrome = 0
#Look at all three digit products and check palindrome
for i in range(startNum,stopNum):
    for j in range(startNum,stopNum):
        product = i*j
        strProd= str(product) 
        if(strProd == strProd[::-1]):   #checks reverse string. Could also use .reverse()
            if(product> pDrome):
                pDrome = product
                
                
print("Largest 3-digit Palindrome: %d" %(pDrome) )