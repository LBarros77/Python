class PizzaError(Exception):
    def __init__(self, pizza, msg):
        Exception.__init__(self, msg)
        self.pizza = pizza

class VeryCheeseError(PizzaError):
    def __init__(self, pizza, cheese, msg):
        PizzaError.__init__(self, pizza, msg)
        self.cheese = cheese

def makePizza(pizza, cheese):
    if pizza not in ["Cheedan", "Calabresa", "Francesa"]:
        raise PizzaError(pizza, "Have not in menu")
    if cheese > 100:
        raise VeryCheeseError(pizza, cheese, "Have very cheese")
    print("Order finalized with sucess!")

for (pz, ch) in [("Cheedan", 120), ("Calabresa", 0), ("Italiana", 50)]:
    try:
        makePizza(pz, ch)
    except VeryCheeseError as vce:
        print(vce, ": ", vce.cheese)
    except PizzaError as pe:
        print(pe, ": ", pe.pizza)
