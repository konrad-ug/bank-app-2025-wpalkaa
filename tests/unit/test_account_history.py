from src.company_account import CompanyAccount
from src.personal_account import PersonalAccount

class TestHistory:
    def test_personal_transfer_history(self):
        account = PersonalAccount("Marcel", "Markowicz", "90031578912")
        account_target = PersonalAccount("Malina", "Lewandowska", "12345678912")
        account.balance = 50.0
        account.transfer_send(30.0, account_target)
        
        assert account.history[-1] == -30.0
        assert account_target.history[-1] == 30.0
        
        
    def test_personal_express_transfer_history(self):
        account = PersonalAccount("Marcel", "Markowicz", "90031578912")
        account_target = PersonalAccount("Malina", "Lewandowska", "12345678912")
        account.balance = 50.0
        account.express_transfer(20.0, account_target)
        
        assert account.history[-2:] == [-20.0, -1.0]
        assert account_target.history[-1] == 20.0
        
        
    def test_company_transfer_history(self):
        account = CompanyAccount("Nazwa", "1234567890")
        account_target = CompanyAccount("Nazwa2", "1234567890")
        account.balance = 50.0
        account.express_transfer(20.0, account_target)
        
        assert account.history[-2:] == [-20.0, -5.0]
        assert account_target.history[-1] == 20.0
        
        
    def test_company_express_transfer_history(self):
        account = CompanyAccount("Nazwa", "1234567890")
        account_target = CompanyAccount("Nazwa2", "1234567890")
        account.balance = 60.0
        account.express_transfer(50.0, account_target)
        
        assert account.history[-2:] == [-50.0, -5.0]
        assert account_target.history[-1] == 50.0
    