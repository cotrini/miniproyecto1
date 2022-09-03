from Employee import Employee
import re
from datetime import date

# Function Section

def addEmployee():
    myEmployee = Employee()
    print("Type employee information\n")
    myEmployee.setName(str(input("Name: ")))
    myEmployee.setId(int(input("Id: ")))
    yearOfBirth = int(input("Year of birth: "))
    mounthOfBirth = int(input("Mounth of birth: "))
    dayOfBirth = int(input("Day of birth: "))
    myEmployee.setBirthDay(yearOfBirth, mounthOfBirth, dayOfBirth)
    myEmployee.setSex(int(input("Gender 1 for female 0 for male: ")))
    myEmployee.setSalary(float(input("Salary: ")))
    myEmployee.setHight(float(input("Hight: ")))
    myEmployeeMaritalStatusIndicator = int(input("Marital status 1 for Single, 2 for Married, 3 for Separate, 4 for Widower: "))
    # Default marital status Single
    myEmployeeMaritalStatus = "Single"
    if(myEmployeeMaritalStatusIndicator == 2):
        myEmployeeMaritalStatus = "Married"
    elif(myEmployeeMaritalStatusIndicator == 3):
        myEmployeeMaritalStatus = "Separate"
    elif(myEmployeeMaritalStatus == 4):
        myEmployeeMaritalStatus = "Widower"
    else:
        pass
    myEmployee.setMaritalStatus(myEmployeeMaritalStatus)

    return myEmployee.getEmployeeRegister()

def loadInformation():
    file = open('employeesDataBase.txt', 'r')
    information = list()
    for line in file:
        employeeData = re.split(';|\n', line)
        employeeData.pop()
        information.append(employeeData)
    file.close()
    return information

# Menu Section


while (True):
    
    print("_"*8)
    print("Welcom to company menu")
    print("_"*8 ,"\n")
    print("1. Add Employees")
    print("-----Reports Section-----")
    print("2. Gender report (show amount of Male and Female employees) ")
    print("3. Age report (show employees on age ranges)") # 18-30, 30-45, 45-60 and more than 60.
    print("4. Financial report (show amount of all salaries in the company per month)")
    print("-----Reports Section-----")
    print("5. Exit")
    selection = int(input("Selection: ") or 6)

    if(selection == 1):
        print("How mutch employees you wanna add today?")
        employesAmount = int(input("Employees amount: "))
        for i in range(employesAmount):
            file = open('employeesDataBase.txt', 'a')
            file.write(addEmployee())
            file.close()

    elif(selection == 2):
        
        women = 0
        mens = 0
        information = loadInformation()
        for info in information:

            if(info[3] == '1'):
                women += 1
            else:
                mens += 1
        print("Women in the company amount: ",women)
        print("Mens in the company: ",mens)

    elif(selection == 3):
        information = loadInformation()
        firstAgeRange = 0
        secondAgeRange = 0
        thirdAgeRange = 0
        fourthAgeRange = 0
        today = date.today()
        for info in information:
            birthDay = re.split('-',info[2])
            years = today.year - int(birthDay[0])
            if(years > 18 and years <= 30):
                firstAgeRange += 1
            elif(years > 30 and years <= 45):
                secondAgeRange += 1
            elif(years > 45 and years <= 60):
                thirdAgeRange += 1
            elif(years > 60):
                fourthAgeRange +=1
        # 18-30, 30-45, 45-60 and more than 60.
        print("The employees amounth with 18 - 30 years old: ", firstAgeRange)
        print("The employees amounth with 30 - 45 years old: ", secondAgeRange)
        print("The employees amounth with 45 - 60 years old: ", thirdAgeRange)
        print("The employees amounth with more than 60 years old: ", fourthAgeRange)


    elif(selection ==4):
        totalSalaryCompany = 0
        information = loadInformation()
        for info in information:
            totalSalaryCompany += float(info[4])
        print('Total company salary: ', totalSalaryCompany)

    elif(selection == 5):
        print("Good Bye")
        exit()

    else:
        print("Make a valid selection please")