#10. Implement encapsulation in a `BankAccount` class with private attributes for `balance` and
#    `account_number`. Include methods for deposit, withdrawal, and balance inquiry.

"""
Encapsulation in object-oriented programming involves hiding the internal state of an object and requiring all interactions to be performed through methods. This helps in protecting the integrity of the data and ensures that it can only be modified in controlled ways.

Here’s how you can implement encapsulation in a BankAccount class with private attributes for balance and account_number, and include methods for deposit, withdrawal, and balance inquiry:

"""
#Example : 
 class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

# Example usage
account = BankAccount("123456789", 1000)
print(f"Account Number: {account.get_account_number()}")
print(f"Initial Balance: ${account.get_balance()}")

account.deposit(500)   # Deposited $500. New balance: $1500.
account.withdraw(200)  # Withdrew $200. New balance: $1300.
print(f"Final Balance: ${account.get_balance()}")  # Output: Final Balance: $1300.

"""

Explanation
Private Attributes:

__account_number and __balance are private attributes (denoted by the double underscores) and cannot be accessed directly from outside the class. This encapsulation ensures that the internal state of the BankAccount object is protected.
Methods:

deposit(amount): Adds the specified amount to the balance if the amount is positive.
withdraw(amount): Subtracts the specified amount from the balance if sufficient funds are available and the amount is positive.
get_balance(): Returns the current balance. This method allows read-only access to the balance.
get_account_number(): Returns the account number. This method allows read-only access to the account number.
Benefits of Encapsulation
Data Protection: By making attributes private, you prevent external code from directly modifying or accessing the internal state.
Controlled Access: Methods like deposit, withdraw, and get_balance provide controlled ways to interact with the data, ensuring that operations are valid and consistent.
Maintenance: Changes to internal data representation can be made without affecting external code that uses the class, as long as the public interface remains consistent.

"""