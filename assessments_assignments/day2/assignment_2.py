def createWallet(balance, username, pin):
    def name():
        nonlocal username
        return username
    def funddeposit(amount):
        nonlocal balance
        balance += amount
    def deposit(amount, upin):
        nonlocal balance, username, pin
        if(upin != pin):
            print("Invalid Pin")
            return
        balance += amount

    def withdraw(amount, upin):
        nonlocal balance, username, pin
        if (upin != pin):
            print("Invalid Pin")
            return
        balance -= amount

    def showbalanace(upin):
        nonlocal balance, username, pin
        if (upin != pin):
            print("Invalid Pin")
            return
        print(username, " balance is ", balance)
    def fundtransfer(amount, wallet, upin):
        nonlocal balance, username, pin
        if(upin!=pin):
            print("Invalid Pin")
            return
        balance -= amount
        wallet["funddeposit"](amount)
        print(amount, " has been transferred from ", username, " to ", wallet["name"]())

    return {"deposit": deposit, "withdraw": withdraw, "showbalance": showbalanace, "fundtransfer": fundtransfer, "name": name, "funddeposit": funddeposit}

wallet1 = createWallet(1000, "porsche", 123)
wallet2 = createWallet(500, "sam", 456)

wallet1["showbalance"](123)
wallet2["showbalance"](456)

wallet1["fundtransfer"](250, wallet2, 123)

wallet1["showbalance"](123)
wallet2["showbalance"](456)

wallet1["withdraw"](100, 123)
wallet1["showbalance"](123)

wallet2["withdraw"](50,789)