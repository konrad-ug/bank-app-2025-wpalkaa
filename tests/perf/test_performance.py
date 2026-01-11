import pytest
import requests

API_URL = "http://127.0.0.1:3005/api/accounts"
TIMEOUT = 0.5

class TestApiPerformance:
    def test_create_delete_account_100_times(self):
        data = {
            "name": "james",
            "surname": "hetfield",
            "pesel": "89092909825"
        }

        for i in range(100):
            r_post = requests.post(API_URL, json=data, timeout=TIMEOUT)
            assert r_post.status_code == 201

            r_delete = requests.delete(f"{API_URL}/{data['pesel']}", timeout=TIMEOUT)
            assert r_delete.status_code == 200

    def test_performance_incoming_transfers_100_times(self):
        data = {
            "name": "james",
            "surname": "hetfield",
            "pesel": "89092909825"
        }
        r = requests.post(API_URL, json=data)
        
        for i in range(100):
            postData = { "amount": 100, "type": "incoming" }
            r = requests.post(f"{API_URL}/{data['pesel']}/transfer", json=postData,timeout=TIMEOUT)
            
            assert r.status_code == 200

        # Sprawdzenie salda końcowego (100 * 10 = 1000)
        r2 = requests.get(f"{API_URL}/{data['pesel']}")
        account = r2.json()

        balance = account["balance"]
        assert balance == 10000.0