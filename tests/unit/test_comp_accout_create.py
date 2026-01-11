from src.company_account import CompanyAccount
import pytest
import requests

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
            
    def test_nip_valid_in_mf_api_error(self, mocker):
        account = CompanyAccount("KONRAD SOŁTYS", "8461627563")
        mocker.patch('requests.get', side_effect=requests.exceptions.ConnectionError("Brak internetu"))

        result = account.nip_valid_in_mf("8461627563")
        
        assert result is False