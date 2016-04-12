# get user input for string
#designate list position for each character in the string
#create a new string with a reverse order of the characters
#Write a function that swaps character based on their position
#Run this swap function thru half of the string
#Deal with the case that you have odd number of cjaracters in the string


def swapPos(stringToSwap, fpos, spos):
    swap = stringToSwap# we turned string into a list
    temp = swap[fpos] # declare a vaiable and we save teh value from the first postion a for the first case
    swap[fpos] = stringToSwap[spos]  #We set to the fpos the value from the second position a becomes d
    swap[spos] = temp # we set the second position (d) to the value in temp which is a(the original first position)

def reverseString(s):
    swapList = list(s)
    l = len(s)
    for t in range(l//2):
         swapPos(swapList, t, l -t-1)
    return "".join(swapList)

print(reverseString("The world is round"))
print(reverseString("abcde"))

#print(swapPos("abcd" ,0,3))

#print(swapPos("abcd" ,1,2))

