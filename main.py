# main.py
from pizza import Margherita, Pepperoni
from toppings import Cheese, Olives , Mushrooms
from payment import PayPal, CreditCard
from Inventory import InventoryManager

def main():
    inventory_manager = InventoryManager()

    print("Welcome to the Pizza Restaurant!")
    
    # Create pizza
    pizza = None
    
    # Choose pizza base
    while True:
        print("\nChoose your base pizza:")
        print("1. Margherita ($150.0)")
        print("2. Pepperoni ($100.0)")
        print("0 => Exit")
        pizza_choice = input("Enter the number of your choice: ")

        if pizza_choice == '0':
            return

        if pizza_choice == '1' and inventory_manager.check_and_decrement("Margherita"):
            pizza = Margherita()  
            break
        elif pizza_choice == '2' and inventory_manager.check_and_decrement("Pepperoni"):
            pizza = Pepperoni()  
            break
        else:
            print("Pizza base unavailable or out of stock!")
    
    # Add toppings
    while True:
        print("\nAvailable toppings:")
        print("1. Cheese ($10.0)")
        print("2. Olives ($5.0)")
        print("3. Mushrooms ($15.0)")
        print("4. Finish order")
        topping_choice = input("Enter the number of your choice: ")

        if topping_choice == "1" and inventory_manager.check_and_decrement("Cheese"):
            pizza = Cheese(pizza)
        elif topping_choice == "2" and inventory_manager.check_and_decrement("Olives"):
            pizza = Olives(pizza)
        elif topping_choice == "3" and inventory_manager.check_and_decrement("Mushrooms"):
            pizza = Mushrooms(pizza)
        elif topping_choice == "4":
            break
        else:
            print("Topping unavailable or out of stock!")

    # Display final pizza details
    print("\nYour order:")
    print(f"Description: {pizza.get_description()}")
    print(f"Total cost: ${pizza.get_cost():.2f}")

    # Show remaining inventory
    print("\nRemaining Inventory:")
    print(inventory_manager.get_inventory())

    # Payment process
    while True:
        print("\nChoose a payment method:")
        print("1. PayPal")
        print("2. Credit Card")
        payment_choice = input("Enter the number of your choice: ")
        
        if payment_choice == "1":
            payment_method = PayPal()
            payment_method.pay(pizza.get_cost())
            break
        elif payment_choice == "2":
            payment_method = CreditCard()
            payment_method.pay(pizza.get_cost())
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
