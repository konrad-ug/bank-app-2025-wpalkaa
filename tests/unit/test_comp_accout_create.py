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
        
