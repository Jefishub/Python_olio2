class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name= name

class SalaryEmployee(Employee):
    def __init__(self,id,name,weekly_salary):
        self.weekly_salary = weekly_salary
        super().__init__(id,name)

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        self.hours_worked = hours_worked
        self.hours_rate = hour_rate
        super().__init__(id,name)

    def calculate_payroll(self):
        return self.hours_rate * self.hours_worked

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        self.commission = commission
        super().__init__(id,name,weekly_salary)

    def calculate_payroll(self):
        return self.weekly_salary+self.commission

emp1 = SalaryEmployee(1,"Jorma", 1500)
print(emp1.name, emp1.calculate_payroll())


emp2 = HourlyEmployee(2,"Pekka", 40, 35)
print(emp2.name, emp2.calculate_payroll())

emp3 = CommissionEmployee(3,"Juhani", 1500,1000)
print(emp3.name, emp3.calculate_payroll())