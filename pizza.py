# pizza.py
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class Margherita(Pizza):
    def __init__(self):
        super().__init__("Margherita Pizza", 5)

class Pepperoni(Pizza):
    def __init__(self):
        super().__init__("Pepperoni Pizza", 6)
