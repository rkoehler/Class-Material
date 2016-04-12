#program begins by showing the menu, and then prompting the user to selelct from the main menu
#selecting "1" gives you a search query where the asks for the patient name, and thent he program find the correct doctor
#selecting "2" gives you a list of all the doctors with their corresponding patients
#seleecting "3" exits the program

listDoctors = ["Sam", "Daniel", "Molly", "Scott"]
patients = [["Bill", "Martha", "Stephanie"]
           ,["Brad"]
           ,["Steven", "Marvin"]
           ,["Gretchen", "Mary", "Mona"]]

menuSelection =  "-1"
    

while menuSelection !=  "3":
    print("Main Menu")
    print(" ")
    print("1. Find the doctor associated with a specific patient")
    print("2. List all doctors with corresponding patients")
    print("3. Exit the program")
    print(" ")

    menuSelection= input("Please select an option number : ")

    if menuSelection == "1":
        print("")
        print(patients)
        print("")
        patientQuery = input("Please choose a patient: ")
        
        patientExists = False
        for patientIndex in range(len(patients)):
            for innerPatientIndex in range(len(patients[patientIndex])):
                if patients[patientIndex][innerPatientIndex] == patientQuery:
                    print("Their doctor is " + listDoctors[patientIndex])
                    print("")
                    patientExists = True
        if patientExists == False:
            print("That is not a patient.")
            print("")
                
    if menuSelection == "2":
        for DoctorIndex in range(len(listDoctors)):
            patientList = patients[DoctorIndex]
            print("Doctor name: " + listDoctors[DoctorIndex])
            print(patientList)

if menuSelection == "3":
        print("Goodbye")

