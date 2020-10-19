class Employee:
    num_of_emps = 0
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@compani.com"
    
    num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee("Lorrayne", "cabral", 1200)
emp2 = Employee("Nathan", "sala", 2300)
'''
emp_str1 = "John-jones-5000"
emp_str2 = "Talita-hener-3900"

new_emp = Employee.from_string(emp_str2)
print(new_emp.__dict__)
print(new_emp.pay)'''

import datetime
my_data = datetime.date(2020, 7, 6)
print(Employee.is_workday(my_data))