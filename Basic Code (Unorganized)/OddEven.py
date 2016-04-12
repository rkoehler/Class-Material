# function checks integer to see if is odd or even
#function divids by 2 two see if it recieves an integer
# result is then boolean

import sys

def oddeven(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False


print(oddeven(204))
print(oddeven(5))
print(oddeven(-2))
print(oddeven(0))
print(oddeven(0.2))
sys.maxsize
