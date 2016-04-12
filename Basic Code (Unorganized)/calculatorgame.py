#game input two numbers and the operation

#2 integers inputs
#1 operation
#computer combines all three to give an output

x = input("Please give me an int: ")
firstInteger = int(x)
#validate input
y = input("Please give me another int: ")
secondInteger = int(y)
z = input("Please select *, /, +, -, %, or ^: ")
if z == "*":
    print(firstInteger*secondInteger)
elif z== "/":
    print(firstInteger/secondInteger)
elif z== "+":
    print(firstInteger+secondInteger)
elif z== "-":
    print(firstInteger-secondInteger)
elif z== "%":
    print(firstInteger%secondInteger)
elif z== "^":
    print(firstInteger^secondInteger)
else:
    print("You gave an invalid answer")
