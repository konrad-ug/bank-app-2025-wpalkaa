class Account:
    def __init__(self):
        self.balance = 0.0
        self.history = []
        self.express_fee = None
    
        # Metody
    def transfer_send(self, amount, target): 
        if amount > 0 and self.balance >= amount:
            self.balance -= amount 
            target.balance += amount
            self.history.append(-amount)
            target.history.append(amount)
    
    def balance_add(self, amount):
        self.balance += amount
        self.history.append(amount)
    
    def express_transfer(self, amount, target):
        if amount > 0 and self.balance >= amount:
            self.transfer_send( amount, target )
            self.balance -= self.express_fee
            
            self.history.append(-self.express_fee)
    
    # To się nie wykona w coverage 
    # def test(self):
    #     return 2 + 4 == 4