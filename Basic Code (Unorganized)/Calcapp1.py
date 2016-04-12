#calculator app

controlVariable = ""
while(controlVariable != "q"):

    x = input("Please give me an int: ")
    firstInteger = int(x)
    #validate input
    y = input("Please give me another int: ")
    secondInteger = int(y)
    z = input("Please select *, /, +, -, %, or ^: OR press q to exit")
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
    elif z== "q":
        controlVariable = z
    else:
        print("You gave an invalid answer")

    if controlVariable != "q":        
        userPrompt = input("Do you want to exit?, y or n?")
        if userPrompt == "y":
            controlVariable = "q"
   
        
    

