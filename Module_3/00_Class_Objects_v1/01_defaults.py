from modules.divider import divider


class BankAccount:
    def __init__(self, account_number=123456, owner="unknown", balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance


account_1 = BankAccount()
print(account_1.account_number)  # 123456
print(account_1.owner)  # unknown
print(account_1.balance)  # 0


divider()


pepito = BankAccount(198345, "Pepito", 1000)
print(pepito.account_number)  # 198345
print(pepito.owner)  # Pepito
print(pepito.balance)  # 1000


divider()


alex = BankAccount(456279, "Alex")
print(alex.account_number)  # 456279
print(alex.owner)  # Alex
print(alex.balance)  # 0
