# payment.py
class PaymentStrategy:
    def pay(self, amount):
        pass

class PayPal(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} via PayPal.")

class CreditCard(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} via Credit Card.")
