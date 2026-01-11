import datetime
from server.smtp import SMTPClient

class Account:
    
    def __init__(self):
        self.balance = 0.0
        self.history = []
        self.express_fee = None
    
        # Metody
    def outgoing_transfer(self, amount): 
        if amount > 0 and self.balance >= amount:
            self.balance -= amount 
            self.history.append(-amount)
            
            return True
        return False
    
    def incoming_transfer(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(amount)
            
            return True
        return False
    
    def express_transfer(self, amount):
        if amount > 0 and self.balance >= amount:
            self.outgoing_transfer(amount)
            self.balance -= self.express_fee
            self.history.append(-self.express_fee)
            return True
        
        return False
    
    
    def send_history_via_email(self, email_address: str) -> bool:
        today_date = datetime.date.today().strftime('%Y-%m-%d')
        subject = "account Transfer History" + today_date
        text = self.history_email_text_template + self.history.__str__()
        return SMTPClient.send(subject, text, email_address)
        
    # To się nie wykona w coverage (test czy działają)
    # def test(self):
    #     return 2 + 4 == 4