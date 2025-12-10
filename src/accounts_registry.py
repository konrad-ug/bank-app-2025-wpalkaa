from src.personal_account import PersonalAccount

class AccountsRegistry:

    def __init__(self):
        self.accounts = []

    def add_account(self, account: PersonalAccount):
        self.accounts.append(account)
    def delete_account(self, account: PersonalAccount):
        self.accounts.remove(account)

    def find_acc_by_pesel(self, pesel):
        for account in self.accounts:
            if account.pesel == pesel:
                return account
        return None
    
    def list_accounts(self):
        return self.accounts
    
    def accounts_amount(self):
        return len(self.accounts)