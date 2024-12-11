# main.py
from pizza import Margherita, Pepperoni
from toppings import Cheese, Olives
from payment import PayPal, CreditCard
from Inventory import InventoryManager

def main():
    # 1. Create a Margherita pizza
    pizza = Margherita()

    # 2. Add toppings (Cheese and Olives)
    pizza = Cheese(pizza)
    pizza = Olives(pizza)

    # 3. Calculate and print total cost and description
    print(f"Pizza Description: {pizza.get_description()}")
    print(f"Total Cost: ${pizza.get_cost()}")

    # 4. Simulate payment with PayPal (or CreditCard)
    payment_method = PayPal()  # Change to CreditCard if needed
    payment_method.pay(pizza.get_cost())

if __name__ == "__main__":
    main()
