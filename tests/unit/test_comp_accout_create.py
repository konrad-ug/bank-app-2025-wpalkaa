from src.company_account import CompanyAccount

class TestCompanyAccount():
    def test_account_create(self):
        account = CompanyAccount("Nazwa", "1234567890")
        assert account.company_name == "Nazwa"
        assert account.nip == "1234567890"
        assert account.balance == 0.0
        
    def test_account_create_wrong_nip(self):
        account = CompanyAccount("Nazwa", "123")
        assert account.company_name == "Nazwa"
        assert account.nip == "Invalid"
        assert account.balance == 0.0
        
    def test_transfer_get(self):
        account = CompanyAccount("Nazwa", "1234567890")
        account.transfer_get(100.0)
        assert account.balance == 100.0
        
    def test_transfer_send(self):
        account = CompanyAccount("Nazwa", "1234567890")
        account_target = CompanyAccount("Nazwa", "1234567890")
        account.balance = 100.0
        account.transfer_send(80.0, account_target)
        
        assert account.balance == 20.0
        assert account_target.balance == 80.0
        
    def test_transfer_send_negative(self):
        account = CompanyAccount("Nazwa", "1234567890")
        account_target = CompanyAccount("Nazwa", "1234567890")
        account.balance = 100.0
        account.transfer_send( -100.0, account_target)
        
        assert account.balance == 100.0
        assert account_target.balance == 0.0