from src.personal_account import PersonalAccount
import pytest

"""
                        # <==== dekorato, mówi kompilatorowi że coś jeszcze musi z tą metodą zrobić, tu że można przekazać
    @pytest.fixture     #          do jakiegoś testu
    def account(self):
        account = PersonalAccount("John", "Doe", "12345678912")
        return account    
        #  yield               # <==== wywołuje test w którym jest użyta metoda i wykonuje coś po tym jeszcze
        #  account.balance = 0
    
    
    
    @pytest.fixture          # Taki inny przykład
    def company_account(self, autouse=True, scope="class"):
       account = PersonalAccount("Comp", "Inc", "12345678912") 
       return account
"""


# Feature 12
class TestLoans:
    @pytest.fixture
    def account(self):
        account = PersonalAccount("John", "Doe", "12345678912")
        return account
    
# To zamiast wszystkich innych testów:
    @pytest.mark.parametrize("history, amount, expected", [
        ([ 1000.0, -200.0, 300.0, 500.0, 400.0], 5000.0, True)
        ([ 100.0, 100.0, 100.0 ], 10000.0, False),
    ],
    ids=[
        "Everything okay"
        "too short history",
    ])
    def test_sumbit_loan(self, history, amount, expected):
        account = PersonalAccount("John", "Doe", "12345678912")
        account.history = history
        result = account.submit_for_loan(amount)
        assert result == expected
    def test_loan(self, account: PersonalAccount, history, amount, expected_result, expected_balance):
        account,history = history
        result = account.sumbit_for_loan(amount)
        assert result == expected_result
        assert account.balance == expected_balance
    
"""
    def test_sumbit_loan_deposits(self, account):
        # account = PersonalAccount("John", "Doe", "12345678912")     
        account.history = [ 10000.0, 1000.0, 100.0, 100.0, 100.0 ]
        
        result = account.submit_for_loan(10000.0)
        
        # assert account.balance == 21300.0
        assert result
        
    def test_sumbit_loan_last_not_deposit_but_over_10000(self, account):
        account.history = [ 10000.0, 1000.0, 100.0, 100.0, -100.0 ]
        
        result = account.submit_for_loan(10000.0)
        
        # assert account.balance == 10200.0
        assert result
        
        
        
    # Result == False
        
        
    def test_sumbit_loan_last_not_deposit(self, account):
        account.history = [ 100.0, 100.0, 100.0, 100.0, -100.0 ]
        
        result = account.submit_for_loan(10000.0)
        
        # assert account.balance == 300.0
        assert not result 
        
    def test_sumbit_loan_two_last_not_deposit(self, account):
        account.history = [ 100.0, 100.0, 100.0, -100.0, -100.0 ]
        
        result = account.submit_for_loan(10000.0)
        
        # assert account.balance == 300.0
        assert not result 
        
    def test_sumbit_loan_too_short_history(self, account):
        account.history = [ 100.0, 100.0 ]
        
        result = account.submit_for_loan(10000.0)
        
        assert not result 

"""