from src.account import Account


class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe", "12345678912")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.pesel == "12345678912"
        assert len(account.pesel) == 11, 'TESTEST' 
        assert account.balance == 0
