import requests
import pytest

url = 'http://localhost:5000/api/accounts'

class TestsApi:
    
    # @pytest.fixture
    # def set_up(self):
    #     data = {
    #         "name": "james",
    #         "surname": "hetfield",
    #         "pesel": "89092909825"
    #     }
    #     r = requests.post(url, json=data)
    #     assert r.status_code == 201
    #     yield
    #     r = requests.get(url)
    #     for account in r.json():
    #         pesel = account["pesel"]
    #         r.delete(f"{url}{"/pesel"}")


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
        response = requests.get(f"{url}{"/count"}")

        assert response.status_code == 200
        assert response.json()["count"]