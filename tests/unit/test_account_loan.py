from src.personal_account import PersonalAccount
import pytest

"""
                        # <==== dekorator, mówi kompilatorowi że coś jeszcze musi z tą metodą zrobić, tu że można przekazać
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
        ([ 1000.0, -200.0, 300.0, 500.0, 400.0], 5000.0, True),
        ([ 100.0, 100.0, 100.0 ], 10000.0, False),
        ([ 10000.0, 1000.0, 100.0, 100.0, -100.0 ], 10000.0, True),
        ([ 100.0, 100.0, 100.0, 100.0, -100.0 ], 10000.0, False),

    ],
    ids=[
        "Everything okay",
        "Too short history",
        "Last transaction not deposit but sum is over 10000",
        "Last transaction not deposit and sum is not over 10000",
    ])
    def test_sumbit_loan(self, account, history, amount, expected):
        account.history = history
        result = account.submit_for_loan(amount)
        assert result == expected

        
    # def test_sumbit_loan(self, history, amount, expected):
    #     account = PersonalAccount("John", "Doe", "12345678912")
    #     account.history = history
    #     result = account.submit_for_loan(amount)
    #     assert result == expected
    # def test_loan(self, account: PersonalAccount, history, amount, expected_result, expected_balance):
    #     account.history = history
    #     result = account.sumbit_for_loan(amount)
    #     assert result == expected_result
    #     assert account.balance == expected_balance