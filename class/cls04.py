class Employee:
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@compani.com"
    
    def fullname(self):
        return f"{self.first} {self.last}"

    def add_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Mensager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emps(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emps(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def str_emps(self):
        for emp in self.employees:
            print("--> ", emp.fullname())
    

dev1 = Developer("Corey", "schafer", 5000, "Pytho")
dev2 = Developer("Victor", "Marks", 6000, "C and C++")

msg1 = Mensager("Carla", "Bastos", 9000, [dev1])
msg2 = Mensager("Carla", "Bastos", 9000, [dev2])

msg1.remove_emps(dev1)
msg1.str_emps()
msg2.str_emps()
print(issubclass(Developer, Employee))