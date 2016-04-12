#function basicExample
def SayHello(name):
    print("Hello :" + name +"Have a good day")

#has return type
def SayHelloWithReturn(name):
    return "Hello :" + name +"Have a good day"

SayHello("Robert")
SayHello("Alfredo")
#we use the return type
mycontent =SayHelloWithReturn("Robert")
print(mycontent + ":)")
