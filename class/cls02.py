class Employee:
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@compani.com"
    
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
emp1 = Employee("Manu", "Tavares", 1000)
emp2 = Employee("Pedro", "martins", 3000)

emp1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print(emp1.__dict__)