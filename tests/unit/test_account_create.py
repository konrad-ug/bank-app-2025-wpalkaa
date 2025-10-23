from src.personal_account import PersonalAccount


class TestAccount:
    def test_account_creation(self):
        account = PersonalAccount("John", "Doe", "12345678912")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.pesel == "12345678912"
        # if len(account.pesel) != 11:
        #     account.pesel = "Invalid"
        #     raise AssertionError("Invalid pesel length")
        assert account.balance == 0
        
    
    # Feature 3
    def test_pesel_too_short(self):
        account = PersonalAccount("Jane", "Smith", "12345")    
        assert account.pesel == "Invalid"

    def test_pesel_too_long(self):
        account = PersonalAccount("Aclie", "Johnson", "12345")
        assert account.pesel == "Invalid"
        
    def test_pesel_too_empty(self):
        account = PersonalAccount("Aclie", "Johnson", "")
        assert account.pesel == "Invalid"
        
        
    
    # Feature 4
    def test_code_is_valid(self):
        account = PersonalAccount("Marek", "Kowalski", "12282978912", "PROM_ab1")
        assert account.balance == 50.0
    
    def test_invalid_code_prefix(self):
        account = PersonalAccount("Marek", "Kowalski", "12282978912", "PRxM_ab1")
        assert account.balance == 0.0
        
    def test_invalid_code_suffix(self):
        account = PersonalAccount("Marek", "Kowalski", "12282978912", "PROM_ab1G")
        assert account.balance == 0.0
        
        
    # Feature 5
    def test_year_2012(self):
        account = PersonalAccount("Marek", "Kowalski", "12282978912", "PROM_ab1") #34 - 2000+
        assert account.balance == 50.0
    
    def test_year_1965(self):
        account = PersonalAccount("Marek", "Kowalski", "65031278912", "PROM_ab1")
        assert account.balance == 50.0

    def test_year_1990(self):
        account = PersonalAccount("Marek", "Kowalski", "90031578912", "PROM_ab1")
        assert account.balance == 50.0

    def test_year_1939(self):
        account = PersonalAccount("Marek", "Kowalski", "39031378912", "PROM_ab1")
        assert account.balance == 0.0