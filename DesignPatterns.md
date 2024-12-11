# Design Patterns and Overengineering

## 1. Factory Method (Pizza Creation)
The Factory Method pattern is used for creating base pizzas. It allows us to add new pizza types (e.g., Margherita, Pepperoni) without modifying the code. This approach is easier to maintain and extend.

## 2. Decorator Pattern (Toppings)
The Decorator Pattern is used to add toppings dynamically. By using decorators, we can add any number of toppings to a pizza without modifying the base pizza class.

## 3. Singleton Pattern (Inventory Manager)
The Singleton Pattern ensures that only one instance of the `InventoryManager` class exists. This guarantees centralized control of ingredients and inventory.

## 4. Strategy Pattern (Payment Methods)
The Strategy Pattern allows us to define different payment methods (e.g., PayPal, CreditCard) and easily switch between them at runtime.

## Overengineering Example
Overengineering would occur if we added complex features that weren’t necessary for the scope of the project. For example, creating a class for discounts when the problem didn’t require it could lead to unnecessary complexity.

```python
class DiscountDecorator(ToppingDecorator):
    def __init__(self, pizza, discount_percent):
        super().__init__(pizza)
        self.discount_percent = discount_percent
    
    def get_cost(self):
        return self.pizza.get_cost() * (1 - self.discount_percent / 100)
