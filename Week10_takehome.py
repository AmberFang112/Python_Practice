from dataclasses import dataclass
@dataclass
class Employee:
    def __init__(self, firstname, lastname, id):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.email = firstname + "." + lastname + "@fanshawe.com"

    def get_employee_detail(self):
        print("Employee name: " + self.firstname + " " + self.lastname)
        print("Employee ID: " + str(self.id))
        print("Email: " + self.email)

class FullTime(Employee):
    def __init__(self, firstname, lastname, id, fixed_salary, benefits):
        super().__init__(firstname, lastname, id)
        self.fixed_salary = fixed_salary
        self.benefits = benefits

    def get_salary(self):
        print("Full-time Salary: " + str(self.fixed_salary))
        print("FUll-time Benefits: " + str(self.benefits))

class PartTime(Employee):
    def __init__(self, firstname, lastname, id, hours_worked, wage):
        super().__init__(firstname, lastname, id)
        self.hours_worked = hours_worked
        self.wage = wage

    def get_salary(self):
        salary = self.hours_worked * self.wage
        print("Part-time Salary: " + str(salary))


class Intern(Employee):
    def __init__(self, firstname, lastname, id, days_worked):
        super().__init__(firstname, lastname, id)
        self.days_worked = days_worked

    def get_salary(self):
        salary = self.days_worked * 50  # Fixed day income 50CAD per day for an intern
        print("Intern Salary: " + str(salary))


# Examples of usage:
p1 = Employee("James", "Will", 98000)
fte1 = FullTime("Nathan", "Huron", 89907, 8000, "Health insurance")
pte1 = PartTime("Emma", "Stone", 91000, 20, 15)
intern1 = Intern("Tom", "Holland", 92000, 5)

fte1.get_employee_detail()
fte1.get_salary()
print()
pte1.get_employee_detail()
pte1.get_salary()
print()
intern1.get_employee_detail()
intern1.get_salary()
