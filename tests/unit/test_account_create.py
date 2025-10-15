from src.account import Account


class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe", "12345678912")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.pesel == "12345678912"
        # if len(account.pesel) != 11:
        #     account.pesel = "Invalid"
        #     raise AssertionError("Invalid pesel length")
        assert account.balance == 0
        
    def test_pesel_too_short(self):
        account = Account("Jane", "Smith", "12345")    
        assert account.pesel == "Invalid"

    def test_pesel_too_long(self):
        account = Account("Aclie", "Johnson", "12345")
        assert account.pesel == "Invalid"
        
    def test_pesel_too_empty(self):
        account = Account("Aclie", "Johnson", "")
        assert account.pesel == "Invalid"