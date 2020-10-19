class cube(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        return "I'm in cube, my name is " + self.name

class dimensions():
    def __init__(self):
        self.width = 20
        self.height = 20

class caracters(cube, dimensions):
    def __init__(self, name):
        from random import choice
        self.color = choice(["Blue", "Gray", "Pupure", "Read"])
        cube.__init__(self, name)
        dimensions.__init__(self)
    
    def query(self):
        return f"{super().query()}, I received: One cube {self.color} of dimension {self.width}px and {self.height}px"

dev1 = caracters("Bruna")
print(dev1.query())