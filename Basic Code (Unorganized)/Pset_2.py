#takes in the input
#breaks down into the factorial

def Factorial(num):
    print(num)
    if num == 1:
        return 1
    else:
        factNum = num * Factorial(num - 1)
        return factNum


Factorial(5)   


