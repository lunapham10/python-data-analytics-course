class Bank_account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = int(balance)

    def add (self, money):
        self.balance += money
        print(f"Added {money} euros to the account")
    
    def spend (self, money):
        if money > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= money
            print(f"Spent {money} euros")
    
    def __str__(self):
        return f"Account name: {self.name}, Account balance: {self.balance}"
    
def main():
    name = input("Name: ")
    balance = input("Balance: ")

    account = Bank_account(name, balance)
    account.add(25)
    account.add(2)
    account.spend(170)
    account.spend(90)

    print(account)

if __name__ == "__main__":
    main()