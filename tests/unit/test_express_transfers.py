from src.company_account import CompanyAccount
from src.personal_account import PersonalAccount

class TestExpressTransfer:
    def test_company_express_perfect(self):
        account = CompanyAccount("Nazwa", "8461627563")
        account.balance = 200.0
        
        result = account.express_transfer(100.0)
        
        assert account.balance == 95.0
        assert result == True
    
    def test_company_express_negative_value(self):
        account = CompanyAccount("Nazwa", "8461627563")
        account.balance = 200.0
        
        result = account.express_transfer(-100.0)
        
        assert account.balance == 200.0
        assert result == False
    
    def test_company_express_fee_negative_balance(self):
        account = CompanyAccount("Nazwa", "8461627563")
        account.balance = 200.0
        
        result = account.express_transfer(200.0)
        
        assert account.balance == -5.0
        assert result == True
        
#=======================================================================
    
    def test_personal_express_prefect(self):
        account = PersonalAccount("Jakub", "Kiczela", "123456789012")
        # account_target = PersonalAccount("Krzysztof", "Woźniak", "123412345678")
        account.balance = 80.0
        
        result = account.express_transfer(70.0)
        
        assert account.balance == 9.0
        assert result == True
        
    def test_personal_express_negative_value(self):
        account = PersonalAccount("Jakub", "Kiczela", "123456789012")
        account.balance = 80.0
        
        result = account.express_transfer(-70.0)
        
        assert account.balance == 80.0
        assert result == False
        
    def test_personal_express_fee_negative_balance(self):
        account = PersonalAccount("Jakub", "Kiczela", "123456789012")
        account.balance = 70.0
        
        result = account.express_transfer(70.0)
        
        assert account.balance == -1.0
        assert result == True