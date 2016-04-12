# function checks integer to see if is odd or even
#function divids by 2 two see if it recieves an integer
# result is then boolean

import sys

def isOdd(num):
    if num % 2 != 0:
        return True
    elif num % 2 == 0:
        return False


print(isOdd(204))
print(isOdd(5))
print(isOdd(-2))
print(isOdd(0))
print(isOdd(0.2))
print(isOdd(sys.maxsize))
print(sys.maxsize)
print(isOdd(-sys.maxsize-1))
