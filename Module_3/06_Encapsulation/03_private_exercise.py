class BankAccount:
    def __init__(self, number, owner, amount=0):
        self.number = number
        self.owner = owner
        self.__amount = amount

    def deposit(self, amount):
        if amount > 0:
            self.__amount += amount
            print(f"\n[+] {amount} added to your account")
        else:
            print("\n[!] Invalid amount")

    def withdraw(self, amount):
        if self.__amount >= amount:
            self.__amount -= amount
            print(f"\n[-] {amount} withdrawn from your account")
        else:
            print("\n[!] Not enough money")

    def show_balance(self):
        print(f"\nBalance: {self.__amount}")


manuel = BankAccount("759351", "Manuel")
manuel.deposit(500)
manuel.withdraw(200)
manuel.show_balance()
