class Account:
    def __init__(self):
        self.balance = 0.0
    
        # Metody
    def transfer_send(self, amount, target): 
        if amount > 0 and self.balance >= amount:
            self.balance -= amount 
            target.balance += amount
    def transfer_get(self, amount):
        self.balance += amount if amount > 0 else 0
    
    
    def express_transfer(self, amount, target, fee):
        if amount > 0 and self.balance >= amount:
            self.transfer_send( amount, target )
            self.balance -= fee
    
    # To się nie wykonaw coverage
    # def test(self):
    #     return 2 + 4 == 4