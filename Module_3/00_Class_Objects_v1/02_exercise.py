from modules.divider import divider


class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

        return f"\n[+] Deposit of ${amount} accepted. Your new balance is ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return f"\n[!] Insufficient funds. Your current balance is ${self.balance}"

        self.balance -= amount

        return f"\n[-] Withdrawal of ${amount} accepted. Your new balance is ${self.balance}"


manuel = BankAccount(187266, "Manuel", 1000)


print(manuel.deposit(500))
print(manuel.withdraw(2000))  # Insufficient funds
print(manuel.withdraw(650))


divider()


daniel = BankAccount(198345, "Daniel", 10)

print(daniel.withdraw(100))
print(daniel.withdraw(5))
