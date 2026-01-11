from src.company_account import CompanyAccount
import pytest

# Feature 13
class TestsCompanyLoans:
    
    @pytest.fixture
    def account(self):
        account = CompanyAccount("Nazwa", "8461627563")
        return account
    
    @pytest.mark.parametrize("history, amount, expected_result, expected_balance", [
        ([1000.0, 1000.0, -1775.0, 1000.0, 1000.0], 500.0, True, 500.0),
        ([10000.0, 10000.0, -1775.0, 1000.0, -1775.0], 5000.0, True, 5000.0),
        ([100.0, -1775.0, 100.0], 10000.0, False, 0.0),
        ([10000.0, 100.0, 500.0], 100.0, False, 0.0),
    ],
    ids=[
        "Everything okay",
        "Everything okay, 2xZUS",
        "Not enough balance",
        "Not ZUS payment",
    ])
    def test_submit_loan(self, account, history, amount, expected_result, expected_balance):
        account.balance = sum(history)
        account.history = history
        result = account.submit_for_loan(amount)
        assert result == expected_result
        assert expected_balance + account.balance == expected_balance + account.balance