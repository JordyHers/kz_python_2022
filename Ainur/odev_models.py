
class Employees:
    def __init__(self,name,surname,age,position):
        self.name = name
        self.surname = surname
        self.age = age
        self.position = position
        
    def getName(self):
        print('name: {}'.format(self.name)) 
        
    def getFullDossier(self):
        return self.name + ' ' + self.surname + ' ' + self.age + ' ' + self.position
        
    def isManager(self):
        return False
    
    def isNotManager(self):
        return True
    
    def isBoss(self):
        return False
        
class Manager(Employees):
    def canFireorHireEmployees():
        return True

class Boss(Manager):
    def CanFireManager():
        return True

list_employees = ['Sarah' , 'Hope' ,'John']
list_managers = ['Susan ']

for name in list_employees:
    if name == 'Sarah':
        Employees_1 = Employees('Sarah','Johanson',28, 'Employee')
        Employees_1.getName()
        print('isManager: {}'.format(Employees_1.isManager()))
        Employees_1.isManager()
    elif name == 'Hope':
        Employees_2 = Employees('Hope','Losse',22, 'Employee')
        Employees_2.getName()
        print('isEmployee: {}'.format(Employees_2.isNotManager()))
        Employees_2.isNotManager()
    elif name == 'John':
        Employees_3 = Employees('John','Richard',35, 'Employee')
        Employees_3.getName()
        print('isEmployee: {}'.format(Employees_3.isNotManager()))
        Employees_3.isNotManager()
    else:
        Employee = Employees(name,'surname')
        Employees.getName()
        print('isEmployee: {}'.format(Employee.isManager()))
        print('Can Not Fire or Hire Employees, Not a Manager or a Boss')
        
for name in list_managers:
    if name == 'Susan':
        Manager_1 = Manager('Susan','Glare',30, 'Manager')
        Manager_1.getName()
        print('isBoss: {}'.format(Manager_1.isBoss()))
        Manager_1.canFireorHireEmployees()

