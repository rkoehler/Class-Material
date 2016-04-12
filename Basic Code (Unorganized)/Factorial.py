#takes in the input
#breaks down into the factorial

def Factorial(num):
    if num == 1:
        return 1
    else:
        factNum = num * Factorial(num - 1)
        return factNum


Factorial(5)
#print(Factorial(5))   


#def Fibonacci(n)
##    print(n)
    #if n = 0
##    else:
        
#        fibo = n

