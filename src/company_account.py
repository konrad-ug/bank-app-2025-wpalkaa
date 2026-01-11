from src.account import Account
import requests
from datetime import date
import os


class CompanyAccount(Account):
    base_url = os.getenv("BANK_APP_MF_URL", "https://wl-api.mf.gov.pl/")
    history_email_text_template = "Company account history:"
    
    
    def __init__(self, company_name, nip, promo_code=None):
        super().__init__()
        self.company_name = company_name
        # self.nip = nip if self.nip_valid(nip) else "Invalid"
        self.express_fee = 5.0
        
        if self.nip_valid(nip):
            if self.nip_valid_in_mf(nip):
                self.nip = nip
            else:
                raise ValueError("Company not registered!")
        else:
            self.nip = "Invalid"
    
    def nip_valid(self, nip):
        if int(nip) and len(nip) == 10:
            return True
        return False
    
    # Feature 18
    def nip_valid_in_mf(self, nip):
        currDate = date.today()
        endpoint = f"{self.base_url}api/search/nip/{nip}?date={currDate}"
        try:
            r = requests.get(endpoint)
            data = r.json()
            
            print(f"MF API response for NIP={nip}: code{r.status_code}\n{data} ")
            
            if r.status_code == 200 and data["result"].get("subject"):
                statusVat = data["result"]["subject"].get("statusVat")
                return statusVat == "Czynny"

            return False
        
        except Exception as error:
            print(f"Error: Couldn't fetched data from MF API: {error}")
            return False
        
    
    # Feature 13
    def submit_for_loan(self, amount):
        zus_payed = any(p == -1775.0 for p in self.history)

        if round(self.balance / amount, 2) >= 2 and zus_payed:
            self.balance += amount
            return True
        else: return False
