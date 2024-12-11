from pizza import Pizza

class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()

class Cheese(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Cheese"
        self.cost = 1

    def get_description(self):
        return self.pizza.get_description() + " + Cheese"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Olives(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Olives"
        self.cost = 0.5

    def get_description(self):
        return self.pizza.get_description() + " + Olives"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost
