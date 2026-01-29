from behave import *
import requests

URL = "http://127.0.0.1:3001"


@step('I create an account using name: "{name}", last name: "{last_name}", pesel: "{pesel}"')
def create_account(context, name, last_name, pesel):
    json_body = {"name": name, "surname": last_name, "pesel": pesel}
    r = requests.post(f"{URL}/api/accounts", json=json_body)
    assert r.status_code == 201

@step('Account registry is empty')
def clear_registry(context):
    r = requests.get(f"{URL}/api/accounts")
    if r.status_code == 200:
        for acc in r.json():
            requests.delete(f"{URL}/api/accounts/{acc['pesel']}")

@step('Number of accounts in registry equals: "{count}"')
def check_count(context, count):
    r = requests.get(f"{URL}/api/accounts/count")
    assert r.status_code == 200
    assert int(r.json()["count"]) == int(count)

@step('Account with pesel "{pesel}" exists in registry')
def check_exists(context, pesel):
    r = requests.get(f"{URL}/api/accounts/{pesel}")
    assert r.status_code == 200

@step('Account with pesel "{pesel}" does not exist in registry')
def check_not_exists(context, pesel):
    r = requests.get(f"{URL}/api/accounts/{pesel}")
    assert r.status_code == 404

@when('I delete account with pesel: "{pesel}"')
def delete_acc(context, pesel):
    r = requests.delete(f"{URL}/api/accounts/{pesel}")
    assert r.status_code == 200

@when('I update "{field}" of account with pesel: "{pesel}" to "{value}"')
def update_field(context, field, pesel, value):
    if field not in ["name", "surname"]:
        raise ValueError(f"Invalid Field: {field}. Must be 'name' or 'surname'.")
    
    json_body = {field: value}
    response = requests.patch(URL + f"/api/accounts/{pesel}", json=json_body)
    assert response.status_code == 200

@then('Account with pesel "{pesel}" has "{field}" equal to "{value}"')
def field_equals_to(context, pesel, field, value):
    response = requests.get(URL + f"/api/accounts/{pesel}")
    assert response.status_code == 200
    data = response.json()
    
    actual_value = str(data.get(field))
    
    if field == "balance" and actual_value.endswith(".0") and "." not in value:
        actual_value = actual_value[:-2]
    
    assert actual_value == str(value), f"Expected {field} to be {value}, but got {actual_value}"
    
@step('I make an incoming transfer of "{amount}" to account with pesel "{pesel}"')
def make_incoming_transfer(context, amount, pesel):
    json_body = {
        "type": "incoming",
        "amount": float(amount)
    }
    response = requests.post(URL + f"/api/accounts/{pesel}/transfer", json=json_body)
    context.last_response_code = response.status_code

@step('I make an outgoing transfer of "{amount}" from account with pesel "{pesel}"')
def make_outgoing_transfer(context, amount, pesel):
    json_body = {
        "type": "outgoing",
        "amount": float(amount)
    }
    response = requests.post(URL + f"/api/accounts/{pesel}/transfer", json=json_body)
    context.last_response_code = response.status_code
