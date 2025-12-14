from flask import Flask, request, jsonify
from src.accounts_registry import AccountsRegistry
from src.personal_account import PersonalAccount

app = Flask(__name__)
registry = AccountsRegistry()

@app.route("/api/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    print(f"Create account request: {data}")
    account = PersonalAccount(data["name"], data["surname"], data["pesel"])
    
    if registry.find_acc_by_pesel(data["pesel"]) is not None:
        print(f"Error 409: Account {data['pesel']} already exists")
        return jsonify(
            {
                "message": "Account with that pesel already exists."
            }
        ), 409
        
    
    registry.add_account(account)
    return jsonify({"message": "Account created"}), 201

@app.route("/api/accounts", methods=['GET'])
def get_all_accounts():
    print("Get all accounts request received")
    accounts = registry.list_accounts()
    accounts_data = [{
        "name": acc.first_name, 
        "surname": acc.last_name, 
        "pesel": acc.pesel, 
        "balance": acc.balance
        } for acc in accounts]
    return jsonify(accounts_data), 200

@app.route("/api/accounts/count", methods=['GET'])
def get_account_count():
    print("Get account count request received")
    count = registry.accounts_amount()

    return jsonify({"count": count}), 200

@app.route("/api/accounts/<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):
    print("Get accounts by pesel request received")
    account = registry.find_acc_by_pesel(pesel)

    if account:
        account_data ={
        "name": account.first_name,
        "surname": account.last_name,
        "pesel": account.pesel,
        "balance": account.balance
        }
        return jsonify(account_data), 200
    else:
        print(f"Error 404: Account {pesel} not found")
        return jsonify({"message": "Account not found"}), 404
        

@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def update_account(pesel):
    account = registry.find_acc_by_pesel(pesel)
    if not account:
        print(f"Error 404: Account {pesel} not found.")
        return jsonify({"message": "Account not found"}), 404
    
    data = request.get_json()
    print(f"Update account request for pesel {pesel}: {data}")
    
    if "name" in data:
        account.first_name = data["name"]
    if "surname" in data:
        account.last_name = data["surname"]
    if "pesel" in data:
        print("Pesel provided, doing nothing...")
        
    print("Account now: ", account.first_name, account.last_name, account.pesel)
    return jsonify({"message": "Account updated"}), 200


@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    print(f"Delete account request for pesel {pesel}")
    account = registry.find_acc_by_pesel(pesel)
    if not account:
        print(f"Error 404: Account {pesel} not found.")
        return jsonify({"message": "Account not found"}), 404
    
    registry.delete_account(account)
    print("Account deleted.")
    
    return jsonify({"message": "Account deleted"}), 200


@app.route("/api/accounts/<pesel>/transfer", methods=['POST'])
def transfer_funds(pesel):
    data = request.get_json()
    print(f"A transfer for {data['amount']} was ordered to {pesel}.")
    
    account = registry.find_acc_by_pesel(pesel)
    if not account:
        return jsonify({"message": "Account not found"}), 404
    
    transferType = data["type"]
    amount = data["amount"]
    
    match transferType:
        case "incoming":
            result = account.incoming_transfer(amount)
        
        case "outgoing":
            result = account.outgoing_transfer(amount,pesel) 
            
        case "express":
            result = account.express_transer(amount, pesel)
            
        case _:
            print(f"Error 400: Type {transferType} not found.")
            return jsonify({
                "message": "Transfer type not found."
            }), 400
    
    if result:
        print(f"Request approved.")
        
        return jsonify({
            "message": "Request approved."
        }), 200
        
    else:
        print(f"Error 422: Request was not approved. Insufficient balance or internal error.")
        
        return jsonify({
            "message": "Request was not approved. Insufficient balance or internal error."
        }), 422