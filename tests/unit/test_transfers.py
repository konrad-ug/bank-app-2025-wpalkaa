from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount


class TestTransfers:
    def test_personal_balance_add(self):
        account = PersonalAccount("Marcel", "Markowicz", "90031578912")
        account.balance_add(500.0)
        
        assert account.balance == 500.0
    
    # Feature 6
    def test_personal_transfer_send(self):
        account = PersonalAccount("Marcel", "Markowicz", "90031578912")
        account_target = PersonalAccount("Malina", "Lewandowska", "12345678912")
        account.balance = 50.0
        account.transfer_send(30.0, account_target)
        
        assert account.balance == 20.0
        assert account_target.balance == 30.0
    
    
    def test_personal_transfer_send_no_money(self):
        account = PersonalAccount("Marcel", "Markowicz", "90031578912")
        account_target = PersonalAccount("Malina", "Lewandowska", "12345678912")
        
        account.transfer_send(30.0, account_target)
        
        assert account.balance == 0.0
        assert account_target.balance == 0.0
        
        
    def test_personal_transfer_send_negative(self):
        account = PersonalAccount("Marcel", "Markowicz", "90031578912")
        account_target = PersonalAccount("Malina", "Lewandowska", "12345678912")
        account.transfer_send( -50.0, account_target)
        
        account.balance = 100.0
        account_target.balance = 100.0
        
        assert account.balance == 100.0
        assert account_target.balance == 100.0
    
    
    def test_company_transfer_send(self):
        account = CompanyAccount("Nazwa", "1234567890")
        account_target = CompanyAccount("Nazwa", "1234567890")
        account.balance = 100.0
        account.transfer_send(80.0, account_target)
        
        assert account.balance == 20.0
        assert account_target.balance == 80.0
        
        
    def test_company_transfer_send_negative(self):
        account = CompanyAccount("Nazwa", "1234567890")
        account_target = CompanyAccount("Nazwa", "1234567890")
        account.balance = 100.0
        account.transfer_send( -100.0, account_target)
        
        assert account.balance == 100.0
        assert account_target.balance == 0.0
         
         
         
         
         
         
         
         
         
         
         
         
         
            
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