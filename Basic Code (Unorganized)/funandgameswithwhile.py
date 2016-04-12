#Samples of while and for loops

#accumulation example
counter = 0
TimesToRun = 13
while(counter < TimesToRun):
    print("Hello")
    counter = counter + 1


#for loop
alist = []
alist2 = ["yey",1,"no"]
print(alist2[0])

#equivalent to for
counter = 0
while counter < 3:
    print(alist2[counter])
    counter = counter + 1

#for print a list
for item in alist2:
    print(item)

#Searching thru a list
studentWeAreLookingFor = "Maria"
programmingClass = ["Robert", "Maria" , "Dave"]
for student in programmingClass:
    if(student == studentWeAreLookingFor):
        print("Yes there is")

print("--- ----")
print(len(programmingClass))
print(range(len(programmingClass)))
# printing position and Item
for index in range(len(programmingClass)):
    print ("Student: "+str(index)+ " Name:"+ programmingClass[index]) 

