from datetime import date

class Employee:

    name : str
    id : int
    birthDay : date
    sex : bool     #1 to female 0 to male
    salary : float
    hight : float
    maritalStatus : str

# Constructor section
    def __init__(self, name, id, birthDay, sex, salary, hight, maritalStatus):

        self.name = name
        self.id = id
        self.birthDay = birthDay
        self.sex = sex
        self.salary = salary
        self.hight = hight
        self.maritalStatus = maritalStatus

# Empty constructor section

    def __init__(self):
        self.name = "NoName"
        self.id = 00000
        self.birthDay = date.today()
        self.sex = 0
        self.salary = 0.0
        self.hight = 0.0
        self.maritalStatus = "NoStatus"
        

# Setters section

    def setName(self, name):
        self.name = name

    def setId(self, id):
        self.id = id

    def setBirthDay(self, year, month, day):
        self.birthDay = date(year, month, day)

    def setSex(self, sex):
        self.sex = sex
    
    def setSalary(self, salary):
        self.salary = salary

    def setHight(self, hight):
        self.hight = hight

    def setMaritalStatus(self, maritalStatus):
        self.maritalStatus = maritalStatus

# Getters section

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getBirthDay(self):
        return self.birthDay

    def getSex(self):
        return self.sex

    def getSalary(self):
        return self.salary

    def getHight(self):
        return self.hight

    def getMaritalStatus(self):
        return self.maritalStatus

    def getEmployeeRegister(self):
        employeeRegister = str(self.name) + ";" + str(self.id) + ";" + str(self.birthDay) + ";" + str(self.sex) + ";" + str(self.salary) + ";" + str(self.hight) + ";" + str(self.maritalStatus) + "|\n" 
        return employeeRegister

# Functions section

    def toString(self):

        print("_"*8)
        print("Employee information: ")
        print("_"*8)
        print("Name: ", self.name)
        print("_"*8)
        print("Id: ",self.id)
        print("_"*8)
        print("Birthday: ", self.birthDay)
        print("_"*8)
        if(self.sex == 1):
            print("Sex: Female")
        else:
            print("Sex: Male")
        print("_"*8)
        print("Salary: ", self.salary)
        print("_"*8)
        print("Hight: ", self.hight)
        print("_"*8)
        print("Marital Status: ", self.maritalStatus)
        print("_"*8)

    def marriedVerifier(self):
        if(self.maritalStatus == "Married"):
            return True
        else:
            return False
