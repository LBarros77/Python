class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@compani.com"
    
    def fullname(self):
        return f"{self.first} {self.last}"

emp1 = Employee("john", "smit", 5000)
emp2 = Employee("Morramed", "sala", 6000)

#print(emp1.email)
#print(emp2.fullname())
#print(Employee.fullname(emp1))