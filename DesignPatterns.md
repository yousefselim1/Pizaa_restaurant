# Design Patterns and Overengineering

## 1. Factory Method (Pizza Creation)
The Factory Method pattern is used for creating base pizzas. It allows us to add new pizza types ( Margherita, Pepperoni) without modifying the code. 

## 2. Decorator Pattern (Toppings)
The Decorator Pattern is used to add toppings dynamically. By using decorators, we can add any number of toppings to a pizza without modifying the base pizza class.

## 3. Singleton Pattern (Inventory Manager)
The Singleton Pattern ensures that only one instance of the `InventoryManager` class exists. This guarantees center control of ingredients and inventory.

## 4. Strategy Pattern (Payment Methods)
The Strategy Pattern allows us to define different payment methods ( PayPal, CreditCard) and easily switch between them at runtime.

## Overengineering Example
Overengineering would occur if we added complex features that weren’t necessary for the scope of the project. For example, creating a class for discounts when the problem didn’t require it could lead to unnecessary complexity.

```python
class DiscountDecorator(ToppingDecorator):
    def __init__(self, pizza, discount_percent):
        self.discount_percent = discount_percent
    
    def get_cost(self):
  
