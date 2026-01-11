import pytest
from src.company_account import CompanyAccount
from src.personal_account import PersonalAccount
import datetime


class TestSendHistoryViaEmail:
    
    email_address = "test@email.com"
    today_date = datetime.date.today().strftime('%Y-%m-%d')
    
    @pytest.fixture
    def perAccount(self):
        acc = PersonalAccount("Marek", "Maruda", "12345678901")
        return acc
    
    @pytest.fixture
    def compAccount(self):
        acc = CompanyAccount("Firmex", "1234567890")
        return acc
    
    
    def test_send_history_via_email_personal_account(self, perAccount, mocker):
        acc = perAccount
        acc.history = [150.0, -50.0]
        
        mock_send = mocker.patch('src.account.SMTPClient.send', return_value=True)
        
        result = acc.send_history_via_email(self.email_address)
        assert result is True 
        mock_send.assert_called_once()
        subject = mock_send.call_args[0][0]
        text = mock_send.call_args[0][1]
        