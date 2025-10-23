from src.company_account import CompanyAccount
from src.personal_account import PersonalAccount

class TestExpressTransfer:
    def test_company_express_perfect(self):
        account = CompanyAccount("Nazwa", "1234567890")
        account_target = CompanyAccount("Nazwa2", "1234567890")
        account.balance = 200.0
        account_target.balance = 50.0
        
        account.express_transfer(100.0, account_target, account.express_fee)
        
        assert account.balance == 95.0
        assert account_target.balance == 150.0
    
    def test_company_express_negative(self):
        account = CompanyAccount("Nazwa", "1234567890")
        account_target = CompanyAccount("Nazwa2", "1234567890")
        account.balance = 200.0
        account_target.balance = 50.0
        
        account.express_transfer(-100.0, account_target, account.express_fee)
        
        assert account.balance == 200.0
        assert account_target.balance == 50.0
    
    def test_company_express_fee_negative(self):
        account = CompanyAccount("Nazwa", "1234567890")
        account_target = CompanyAccount("Nazwa2", "1234567890")
        account.balance = 200.0
        account_target.balance = 50.0
        
        account.express_transfer(200.0, account_target, account.express_fee)
        
        assert account.balance == -5.0
        assert account_target.balance == 250.0
        
#=======================================================================
    
    def test_personal_express_prefect(self):
        account = PersonalAccount("Jakub", "Kiczela", "123456789012")
        account_target = PersonalAccount("Krzysztof", "Woźniak", "123412345678")
        account.balance = 80.0
        account_target.balance = 0
        
        account.express_transfer(70.0, account_target, account.express_fee)
        
        assert account.balance == 9.0
        assert account_target.balance == 70.0
        
    def test_personal_express_negative(self):
        account = PersonalAccount("Jakub", "Kiczela", "123456789012")
        account_target = PersonalAccount("Krzysztof", "Woźniak", "123412345678")
        account.balance = 80.0
        account_target.balance = 0
        
        account.express_transfer(-70.0, account_target, account.express_fee)
        
        assert account.balance == 80.0
        assert account_target.balance == 0.0
        
    def test_personal_express_fee_negative(self):
        account = PersonalAccount("Jakub", "Kiczela", "123456789012")
        account_target = PersonalAccount("Krzysztof", "Woźniak", "123412345678")
        account.balance = 70.0
        account_target.balance = 0
        
        account.express_transfer(70.0, account_target, account.express_fee)
        
        assert account.balance == -1.0
        assert account_target.balance == 70.0