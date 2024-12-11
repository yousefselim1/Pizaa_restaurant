from abc import ABC, abstractmethod

# Base Pizza class
class Pizza(ABC):
    def __init__(self):
        self.description = "Unknown Pizza"
        self.cost = 0

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


# Margherita Pizza
class Margherita(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margherita Pizza"
        self.cost = 150.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


# Pepperoni Pizza
class Pepperoni(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Pepperoni Pizza"
        self.cost = 100.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost
