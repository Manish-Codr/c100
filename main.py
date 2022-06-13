# checkBalance,
# BalanceEnquiry,
# CashWithDrawl,
# InsertCard
class Atm(object):
    def __int__(self, cardnumber, pin):
        self.cardnumber = cardnumber,
        self.pin = pin

    def checkbalance(self):
        balance = 500000
        print("balance = 50,000")

    def cashwithdrawl(self, amount):
        newamount = 50000 - amount
        print("you have withdrawn amount" + str(amount) + ".your remaining balance is" + str(newamount))


def main():
    cardnumber = input("Enter Your Card Number: ")
    pin = input("Enter Your Pin Number: ")
    newuser = Atm(cardnumber, pin)
    print("Choose Your Activity: ")
    print("1. BalanceEnquiry                               2. CashWithDrawl")
    action = int(input("Enter Activity Number"))
    if action == 1:
        newuser.checkbalance()
    elif action == 2:
        amount = int(input("Enter The Amount You Want To Withdraw: "))
        newuser.cashwithdrawl()
    else:
        print("Enter A Valid Number")


if __name__ == "__main__":
    main()
