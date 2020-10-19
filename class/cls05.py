class Employee:
    percent = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@compani.com"

    def fullname(self):
        return f"{self.first} {self.last}"
    
    def cont(self):
        self.pay = int(self.pay * self.percent)
    
    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"
    
    def __str__(self):
        return f"{self.fullname} - {self.email}"
    
    def __iadd__(self, other):
        return self.pay + other.pay
    
    def __sub__(self, other):
        return self.pay - other.pay


emp1 = Employee("DG", "Production", 9000)
emp2 = Employee("Jose", "Panelas", 1000)

print(emp1 + emp2)
print(emp1 - emp2)