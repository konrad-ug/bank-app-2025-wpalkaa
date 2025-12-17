from src.company_account import CompanyAccount
import pytest

class TestCompanyAccount():
    def test_all_okay(self):
        account = CompanyAccount("KONRAD SOŁTYS", "8461627563")
        assert account.company_name == "KONRAD SOŁTYS"
        assert account.nip == "8461627563"
        
    def test_too_short_nip(self):
        account = CompanyAccount("Nazwa", "123")
        assert account.company_name == "Nazwa"
        assert account.nip == "Invalid"
        
    def test_doesnt_exists_in_mf_base(self):
        with pytest.raises(ValueError, match="Company not registered!"):
            CompanyAccount("NIEMATAKIEJ", "1234567890")
            
    
