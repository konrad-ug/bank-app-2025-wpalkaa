import requests
import pytest

BASE_URL = "http://localhost:3001/api/accounts"

class TestMongoPersistence:

    @pytest.fixture(autouse=True)
    def cleanup(self):
        r = requests.get(BASE_URL)
        if r.status_code == 200:
            for acc in r.json():
                requests.delete(f"{BASE_URL}/{acc['pesel']}")
        yield

    def test_save_accounts_empty_registry(self):
        response = requests.post(f"{BASE_URL}/save")
        assert response.status_code == 400
        assert response.json()["message"] == "No accounts to save"

    def test_save_and_load_flow(self):
        user_data = {
            "name": "James",
            "surname": "Hetfield",
            "pesel": "89092909825"
        }
        
        create_resp = requests.post(BASE_URL, json=user_data)
        assert create_resp.status_code == 201

        save_resp = requests.post(f"{BASE_URL}/save")
        assert save_resp.status_code == 200
        assert save_resp.json()["message"] == "Accounts successfully saved to MongoDB"

        check_empty = requests.get(BASE_URL)
        assert len(check_empty.json()) == 0

        load_resp = requests.post(f"{BASE_URL}/load")
        assert load_resp.status_code == 200
        assert load_resp.json()["accounts"] == 1

        get_all = requests.get(BASE_URL)
        accounts = get_all.json()
        assert len(accounts) == 1
        
        loaded_account = accounts[0]
        assert loaded_account["pesel"] == user_data["pesel"]
        assert loaded_account["name"] == user_data["name"]
        assert loaded_account["surname"] == user_data["surname"]