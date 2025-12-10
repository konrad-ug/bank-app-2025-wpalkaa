import requests
import pytest

url = 'http://localhost:5000/api/accounts'

class TestsApi:
    
    @pytest.fixture(scope="function", autouse=True)
    def set_up(self):
        data = {
            "name": "james",
            "surname": "hetfield",
            "pesel": "89092909825"
        }
        r = requests.post(url, json=data)
        assert r.status_code == 201

        yield

        r = requests.get(url)
        for account in r.json():
            pesel = account["pesel"]
            requests.delete(f"{url}/{pesel}")
    

    def test_create_account(self):
        data = {
            "name": "james",
            "surname": "hetfield",
            "pesel": "89092909825"
        }

        r = requests.post(url, json=data)
        
        assert r.status_code == 201
        assert r.json()["message"] == 'Account created'

    def test_count(self):
        response = requests.get(f"{url}{'/count'}")

        assert response.status_code == 200
        assert response.json()["count"] == 1
        
    def test_get_account_by_pesel(self):
        
        pesel = "89092909825"
        r = requests.get(f"{url}/{pesel}")
        
        assert r.status_code == 200
        
        data = r.json()
        
        assert data["name"] == "james"
        assert data["surname"] == "hetfield"
        assert data["pesel"] == "89092909825"
               
    def test_pesel_doesnt_exist_in_base(self):
        
        pesel = "12345678901"
        r = requests.get(f"{url}/{pesel}")
        
        assert r.status_code == 404
        
        data = r.json()
        
        assert data["message"] == "Account not found"
        
    def test_update_account(self):
        
        patch_pesel = "89092909825"
        patch_data = {
            "name": "Joanna",
            "surname": "Bak"
        }
        
        r = requests.patch(f"{url}/{patch_pesel}", json=patch_data)
        assert r.status_code == 200
        
        r2 = requests.get(f"{url}/{patch_pesel}")
        data = r2.json()
        
        assert data["name"] == "Joanna"
        assert data["surname"] == "Bak"
        
    def test_update_account_pesel_provided(self):
        
        patch_pesel = "89092909825"
        patch_data = {
            "name": "Joanna",
            "surname": "Bąk",
            "pesel": "12345678901"
        }
        
        r = requests.patch(f"{url}/{patch_pesel}", json=patch_data)
        assert r.status_code == 200
        
        r2 = requests.get(f"{url}/{patch_pesel}")
        data = r2.json()
        
        assert data["name"] == "Joanna"
        assert data["surname"] == "Bąk"
        assert data["pesel"] == patch_pesel
        
    def test_patch_account_pesel_not_found(self):
        
        patch_pesel = "12345678901"
        patch_data = {
            "name": "Joanna",
            "surname": "Bąk"
        }
        
        r = requests.patch(f"{url}/{patch_pesel}", patch_data)
        assert r.status_code == 404
        
        data = r.json()
        
        assert data["message"] == "Account not found"
        
        