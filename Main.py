from Employee import Employee
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



# Menu Section

file = open('employeesDataBase.txt', 'w')
while (True):
    
    print("_"*8)
    print("Welcom to company menu")
    print("_"*8 ,"\n")
    print("1. Add Employees")
    print("-----Reports Section-----")
    print("2. Gender report (show amount of Male and Female employees) ")
    print("3. Age report (show employees on age ranges)") # 18-30, 30-45, 45-60 y more than 60.
    print("4. Financial report (show amount of all salaries in the company per month)")
    print("-----Reports Section-----")
    print("5. Exit")
    selection = int(input("Selection: "))

    if(selection == 1):
        print("How mutch employees you wanna add today?")
        employesAmount = int(input("Employees amount: "))
        for i in range(employesAmount):
            file.write(addEmployee())
    elif(selection == 2):
        print("reading....")
        for line in file:
            print("Employee")
            line.split("|")
            print(line)
    elif(selection == 5):
        print("Good Bye")
        exit()