from src.account import Account

class PersonalAccount(Account):
    def __init__(self, first_name, last_name, pesel, promo_code=None):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.express_fee = 1.0
        
        self.pesel = pesel if self.is_pesel_valid(pesel) else "Invalid"
        self.balance += 50.0 if self.is_promo_code_valid(promo_code) and self.year_is_after_1965(pesel) else 0.0
        
        
    def submit_for_loan(self, amount):
        if len(self.history) < 5: return False
        
        ifDeposit = [i > 0 for i in self.history]
        lastFiveSum = sum(self.history[-5:])
        
        if all(ifDeposit) or lastFiveSum > amount:
            self.balance += amount
            self.history.append(amount)
            return True        
        else:
            return False
        
        
    # Warunki konstruktora
    def is_pesel_valid(self, pesel):
        if pesel and len(pesel) == 11:
            return True
        return False
    
    def is_promo_code_valid(self, promo_code):
        if promo_code and promo_code.startswith("PROM_") and len(promo_code) == 8:
            return True
        return False
    
    def year_is_after_1965(self, pesel):
        month = "".join( map( str, pesel[2:4]) )
        year = "".join( map( str, pesel[:2]) )
        
        if ( int(month) < 20 ) and ( int(year) < 65 ):
            return False
        return True
    
    
