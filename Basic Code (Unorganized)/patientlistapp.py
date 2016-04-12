#hospital list

#patient position = Doctor position
#ask user for patient name
#tell program to figure out position of patient name
#tell program to figure out position of doctor name
#tell program to match postion of names




listDoctors = ["Mark", "Steve", "Wayne", "Thomas"]
patients = [["Todd", "Dan"]
            , ["Tim", "Robert"]
            , ["Maria"]
            , ["Jose"]]


patientWeAreLookingFor = input("Please give me a patient name: ")

for patientIndex in range(len(patients)):
    for innerPatientIndex in range(len(patients[patientIndex])):
        if patients[patientIndex][innerPatientIndex] == patientWeAreLookingFor:
            print("His Doctor is " + listDoctors[patientIndex])

#    if patients[patientIndex] == patientWeAreLookingFor:
#


# Homework
#1- Application allow to exit
#    b. Print Doctor's name and list of patients
# sample menu
#    1. To look for patient's doctor
#    2. Print all doctors and patients
#    3. Exit
# 4. add data
#5. store 
        
# Figure out a design for your calendar application
# Implement the start menu for it.


#Meeting 31st at 11am  
