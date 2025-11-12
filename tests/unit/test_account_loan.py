from src.personal_account import PersonalAccount
import pytest

class TestLoans:
    
                            # <==== dekorato, mówi kompilatorowi że coś jeszcze musi z tą metodą zrobić, tu że można przekazać
    @pytest.fixture    #          do jakiegoś testu
    def account(self):
        account = PersonalAccount("John", "Doe", "12345678912")
        return account
        
        #  yield               # <==== wywołuje test w którym jest użyta metoda i wykonuje coś po tym jeszcze
        #  account.balance = 0
    
    @pytest.fixture
    def company_account(self, autouse=True, scope="class"):
        account = PersonalAccount("Comp", "Inc", "12345678912") # dla przykładu tylko
        return account
     
    def test_sumbit_loan_deposits(self, account):
        # account = PersonalAccount("John", "Doe", "12345678912")     
        account.history = [ 10000.0, 1000.0, 100.0, 100.0, 100.0 ]
        
        result = account.submit_for_loan(10000.0)
        
        # assert account.balance == 21300.0
        assert result == True
        
    def test_sumbit_loan_last_not_deposit_but_over_10000(self, account):
        account.history = [ 10000.0, 1000.0, 100.0, 100.0, -100.0 ]
        
        result = account.submit_for_loan(10000.0)
        
        # assert account.balance == 10200.0
        assert result == True
        
        
        
    # Result == False
        
        
    def test_sumbit_loan_last_not_deposit(self, account):
        account.history = [ 100.0, 100.0, 100.0, 100.0, -100.0 ]
        
        result = account.submit_for_loan(10000.0)
        
        # assert account.balance == 300.0
        assert result == False
        
    def test_sumbit_loan_two_last_not_deposit(self, account):
        account.history = [ 100.0, 100.0, 100.0, -100.0, -100.0 ]
        
        result = account.submit_for_loan(10000.0)
        
        # assert account.balance == 300.0
        assert result == False
        
    def test_sumbit_loan_too_short_history(self, account):
        account.history = [ 100.0, 100.0 ]
        
        result = account.submit_for_loan(10000.0)
        
        assert result == False

