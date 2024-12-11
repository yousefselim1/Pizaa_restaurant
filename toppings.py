from pizza import Pizza

class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()


class Cheese(ToppingDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)
        self.description = "Cheese"
        self.cost = 10.0

    def get_description(self):
        return self.pizza.get_description() + " + Cheese"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost


class Olives(ToppingDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)
        self.description = "Olives"
        self.cost = 5.0

    def get_description(self):
        return self.pizza.get_description() + " + Olives"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost


class Mushrooms(ToppingDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)
        self.description = "Mushrooms"
        self.cost = 15.0

    def get_description(self):
        return self.pizza.get_description() + " + Mushrooms"

    def get_cost(self):
        return self.pizza.get_cost() + self.cost
