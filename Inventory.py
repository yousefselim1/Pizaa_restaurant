from abc import ABC, abstractmethod

# Singleton Inventory Manager
class InventoryManager:
    _instance = None
    _inventory = {
        "Margherita": 10,
        "Pepperoni": 10,
        "Cheese": 15,
        "Olives": 10,
        "Mushrooms": 12,
    }

    def check_and_decrement(self, item: str) -> bool:

        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False

    def get_inventory(self):
        return self._inventory

    @classmethod
    def get_instance(l):
        if l._instance is None:
            l._instance = InventoryManager()
        return l._instance