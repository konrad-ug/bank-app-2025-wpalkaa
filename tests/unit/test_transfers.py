from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount


class TestTransfers:
    def test_personal_incoming(self):
        account = PersonalAccount("Marcel", "Markowicz", "90031578912")
        result = account.incoming_transfer(500.0)
        
        assert account.balance == 500.0
        assert result == True
        
    def test_personal_incoming_negative_value(self):
        account = PersonalAccount("Marcel", "Markowicz", "90031578912")
        result = account.incoming_transfer(-500.0)
        
        assert account.balance == 0.0
        assert result == False
        
    # Feature 6
    def test_personal_outgoing(self):
        account = PersonalAccount("Marcel", "Markowicz", "90031578912")
        account.balance = 50.0
        result = account.outgoing_transfer(30.0)
        
        assert account.balance == 20.0
        assert result == True
    
    
    def test_personal_outgoing_no_money(self):
        account = PersonalAccount("Marcel", "Markowicz", "90031578912")
        
        result = account.outgoing_transfer(30.0)
        
        assert account.balance == 0.0
        assert result == False
        
        
    def test_personal_outgoing_negative_value(self):
        account = PersonalAccount("Marcel", "Markowicz", "90031578912")
        account.balance = 100.0
        
        result = account.outgoing_transfer(-50.0)
        
        assert account.balance == 100.0
        assert result == False
    
    
    def test_company_outgoing(self):
        account = CompanyAccount("Nazwa", "8461627563")
        account.balance = 100.0
        
        result = account.outgoing_transfer(80.0)
        
        assert account.balance == 20.0
        assert result == True
        
        
    def test_company_outgoing_negative_value(self):
        account = CompanyAccount("Nazwa", "8461627563")
        account.balance = 100.0
        result = account.outgoing_transfer( -100.0)
        
        assert account.balance == 100.0
        assert result == False
         
         
         
         
         
         
         
         
         
         
         
         
         
            
    # Jego testy
    
    # def test_incoming_transfer(self):
    #     account = Account("John", "Doe", "12345678901")
    #     account.incoming_transfer(100.0)
    #     assert account.balance == 100.0
        
    # def test_outgoing_transfer(self):
    #     account = Account("John", "Doe", "12345678901")
    #     account.balance = 70.0
    #     account.outgoing_transfer(50.0)
    #     assert account.balance == 20.0