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

        self.__name = name
        self.__id = id
        self.__birthDay = birthDay
        self.__sex = sex
        self.__salary = salary
        self.__hight = hight
        self.__maritalStatus = maritalStatus

# Empty constructor section

    def __init__(self):
        self.__name = "NoName"
        self.__id = 00000
        self.__birthDay = date.today()
        self.__sex = 0
        self.__salary = 0.0
        self.__hight = 0.0
        self.__maritalStatus = "NoStatus"
        

# Setters section

    def setName(self, name):
        self.__name = name

    def setId(self, id):
        self.__id = id

    def setBirthDay(self, year, month, day):
        self.__birthDay = date(year, month, day)

    def setSex(self, sex):
        self.__sex = sex
    
    def setSalary(self, salary):
        self.__salary = salary

    def setHight(self, hight):
        self.__hight = hight

    def setMaritalStatus(self, maritalStatus):
        self.__maritalStatus = maritalStatus

# Getters section

    def getName(self):
        return self.__name

    def getId(self):
        return self.__id

    def getBirthDay(self):
        return self.__birthDay

    def getSex(self):
        return self.__sex

    def getSalary(self):
        return self.__salary

    def getHight(self):
        return self.__hight

    def getMaritalStatus(self):
        return self.__maritalStatus

    def getEmployeeRegister(self):
        employeeRegister = str(self.getName()) + ";" + str(self.getId()) + ";" + str(self.getBirthDay()) + ";" + str(self.getSex()) + ";" + str(self.getSalary()) + ";" + str(self.getHight()) + ";" + str(self.getMaritalStatus()) + "\n" 
        return employeeRegister

# Functions section

    def toString(self):  # SHOW FUNCTION

        print("_"*8)
        print("Employee information: ")
        print("_"*8)
        print("Name: ", self.getName())
        print("_"*8)
        print("Id: ",self.getId())
        print("_"*8)
        print("Birthday: ", self.getBirthDay())
        print("_"*8)
        if(self.sex == 1):
            print("Sex: Female")
        else:
            print("Sex: Male")
        print("_"*8)
        print("Salary: ", self.getSalary())
        print("_"*8)
        print("Hight: ", self.getHight())
        print("_"*8)
        print("Marital Status: ", self.getMaritalStatus())
        print("_"*8)

    def marriedVerifier(self):
        if(self.getMaritalStatus() == "Married"):
            return True
        else:
            return False
