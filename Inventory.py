# inventory.py
class InventoryManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InventoryManager, cls).__new__(cls)
            cls._instance.ingredients = {'Cheese': 10, 'Olives': 10, 'Mushrooms': 10}
        return cls._instance

    def check_availability(self, ingredient):
        return self.ingredients.get(ingredient, 0) > 0
