from src.account import Account


class CompanyAccount(Account):
    def __init__(self, company_name, nip, promo_code=None):
        super().__init__()
        self.company_name = company_name
        self.nip = nip if self.nip_valid(nip) else "Invalid"
        self.express_fee = 5.0
        
    
    
    def nip_valid(self, nip):
        if int(nip) and len(nip) == 10:
            return True
        return False