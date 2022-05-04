class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account


Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, True)

print(Jeff.withdraw(2), 'Jeff has 68.')
print(Joe.check(Jeff, 50), 'Joe has 120 and Jeff has 18.')
print(Jeff.check(Joe, 80), 'Jeff has 98 and Joe has 40.')
print(Jeff.add_cash(20), 'Jeff has 118.')