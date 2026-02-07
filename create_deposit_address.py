import json
import uuid
import requests
from dotenv import load_dotenv
from get_auth_token import get_auth_token

load_dotenv()

access_token = get_auth_token()

# create seller profile
endpoint = "https://api.sandbox.paxos.com/v2/transfer/deposit-addresses"
ref_id = f"da_{uuid.uuid4()}"
res = requests.post(
    endpoint, 
    json={
        "profile_id": "a7a99e88-bd7b-4154-a33b-7b8edfd79a71", # Peter Seller 
        "crypto_network": "SOLANA",
        "ref_id": ref_id, # we generate a random ref_id for each request
        "conversion_target_asset": "USD"
    }, 
    headers={
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    })

if res.status_code != 200:
    print("Deposit address creation failed:", res.status_code, res.text)
    exit(1)

deposit_address = res.json()
print(json.dumps(deposit_address, indent=2))

print(f"Deposit address created: {deposit_address.get('address')} with ref_id {ref_id}")