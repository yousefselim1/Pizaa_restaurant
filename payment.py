from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# PayPal payment method
class PayPal(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal.")


# Credit Card payment method
class CreditCard(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card.")
