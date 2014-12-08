from cisc106 import *

class Employee:
    """

    An employee is a person who works for a company.

    position -- string
    salary -- integer

    """

    def __init__(self,position,salary,age):
        self.position = position
        self.salary = salary
        self.age = age

    """

    def employee_function(aEmployee,...):
    return aEmployee.position
    aEmployee.salary
    
    """

    def employee_status(self):
        """

        Gives you the positon and salary of the employee
        Employee -- Employee
        return -- string
        
        """

        print(self.position)
        print("The Salary of the employee is", self.salary)
        print("The age of the employee is", self.age)

        return(self.position)
    
    def change_salary(self,change):
        
        """
        Changes the position of the employee

        Position - Position
        return - String

        """

        self.salary = self.salary + (self.salary * change)
    


aEmployee1 = Employee("CEO",500000,24)
aEmployee2 = Employee("Programmer",100000,19)

aEmployee1.employee_status
aEmployee2.change_salary(.50)

assertEqual(aEmployee1.employee_status(),'CEO')
