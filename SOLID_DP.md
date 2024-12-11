# SOLID Principles and Design Patterns

## 1. Factory Method (Pizza Creation)
- **SRP**: The `Pizza` classes each handle a single responsibility—pizza creation.
- **OCP**: The pizza creation process can be extended with new pizza types (e.g., `Vegetarian`, `Hawaiian`) without modifying existing code.
- **LSP**: We can substitute any subclass (e.g., `Margherita`, `Pepperoni`) wherever a `Pizza` object is expected.
- **ISP**: No interface segregation needed as we are working with a single abstract class.
- **DIP**: High-level logic (order process) depends on the abstract `Pizza` class, not specific pizza types.

## 2. Decorator Pattern (Toppings)
- **SRP**: Each topping class adds one responsibility (adding a topping) to the pizza.
- **OCP**: We can add new toppings (e.g., `Mushrooms`) without modifying existing topping classes.
- **LSP**: A topping can be substituted for any other topping or base pizza without affecting functionality.
- **ISP**: Decorators implement the same interface, ensuring they are interchangeable.
- **DIP**: We depend on the `Pizza` base class and the `ToppingDecorator` interface.

## 3. Singleton Pattern (Inventory Manager)
- **SRP**: The `InventoryManager` is responsible only for managing ingredient availability.
- **OCP**: The inventory system can be extended with more inventory management features without changing the existing structure.
- **LSP**: The `InventoryManager` class can be substituted with any other class that implements the same functionality.
- **ISP**: We are not separating interfaces in this case as it’s a simple singleton.
- **DIP**: The inventory management relies on a singleton instance that controls ingredient data.

## 4. Strategy Pattern (Payment Methods)
- **SRP**: The `PayPal` and `CreditCard` classes are each focused on a single responsibility—processing payments.
- **OCP**: We can add more payment methods (e.g., `ApplePay`, `GooglePay`) without modifying existing payment classes.
- **LSP**: Payment methods can be substituted easily.
- **ISP**: Payment strategies provide distinct interfaces for each payment method.
- **DIP**: The payment strategy is abstract, and the payment context depends on it.




