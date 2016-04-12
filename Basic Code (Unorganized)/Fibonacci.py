#fibonacci requires 2 seeding inputs
#fibonacci takes those two inputs and adds them together to get the resultant fibonacci number

def Fibo(n):
    if n == 0  or  n ==1:
        return 1
    else:
        result = Fibo(n-1) + Fibo(n-2)
        return result

print(Fibo(5))
