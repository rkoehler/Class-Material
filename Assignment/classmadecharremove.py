#function Remove Char decomposition
#function signature - Known
#string to list -Known
#loop thru the first list -Known
#Figure out if character is in the second list -> Second function
#if true remove from the first
    #replace with ''
#move to the next

#function isPresent decomposition
#function signature - Known
#Iterate thru charsToRemove -Known
#Compare charInList to inputChar

def isPresent(aChar , charsToRemove):
    for charInList in charsToRemove:
        if aChar == charInList:
            return True
    return False


def removeChar(s , charsToRemove):
    theList = list(s)
    for position in range(len(theList)):
        #print("The position that came out from the list in range")
        #print(position)
        #print("the character from the list")
        #print(theList[position])
        if isPresent(theList[position], charsToRemove):
            theList[position] = ''
    return "".join(theList)


print(removeChar("alfredoalvarez", "al"))
print(removeChar("alfredo", "fr"))
print(removeChar("", "sasdasd"))
print(removeChar("asda", ""))
            

#tictactoe board and accept a parameter to print a 0 in a pos
#swapletters in a given string swapletters(string, aChar, swap with)
#count all the different letters in a string return void it just prints the counts out            
