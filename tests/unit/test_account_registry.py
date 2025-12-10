from src.accounts_registry import AccountsRegistry
from src.personal_account import PersonalAccount
import pytest

# Feature 14
class TestAccountsRegistry:

    @pytest.fixture
    def accounts(self):
        acc1 = PersonalAccount("Marek", "Kowalski", "12282978912")
        acc2 = PersonalAccount("Justyna", "Kowalczyk", "06212978912")
        return acc1, acc2
    
    @pytest.fixture
    def accountsRegistry(self, accounts):
        acc1, acc2 = accounts
        accountsRegistry = AccountsRegistry()

        accountsRegistry.accounts = [acc1, acc2]
        
        return accountsRegistry



    def test_add_account(self, accounts ):
        accountsRegistry = AccountsRegistry()
        acc1, acc2 = accounts

        accountsRegistry.add_account(acc1)
        accountsRegistry.add_account(acc2)

        assert len(accountsRegistry.accounts) == 2


    def test_find_pesel(self, accountsRegistry, accounts):

        acc = accountsRegistry.find_acc_by_pesel("12282978912")
        assert acc == accountsRegistry.accounts[0]

    def test_not_found_pesel(self, accountsRegistry):

        acc = accountsRegistry.find_acc_by_pesel("11111111111")
        assert acc is None


    def test_delete_account(self, accountsRegistry):
        acc = accountsRegistry.find_acc_by_pesel("12282978912")
        accountsRegistry.delete_account(acc)

        assert len(accountsRegistry.accounts) == 1
        assert accountsRegistry.accounts[0].pesel == "06212978912"


    def test_account_list(self, accountsRegistry, accounts):

        accounts = accountsRegistry.list_accounts()

        assert accounts == accountsRegistry.accounts


    def test_accounts_amount(self, accountsRegistry):
        assert accountsRegistry.accounts_amount() == 2