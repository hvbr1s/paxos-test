import requests
from dotenv import load_dotenv
from get_auth_token import get_auth_token

load_dotenv()

access_token = get_auth_token()

# create seller profile
profile_url = "https://api.sandbox.paxos.com/v2/profiles"
profile_response = requests.post(
    profile_url, 
    json={
        "nickname": "Peter Seller",
        "description": "Stablecoin Transfers to Fordefi"
    }, 
    headers={
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
)

if profile_response.status_code != 200:
    print("Profile creation failed:", profile_response.status_code, profile_response.text)
    exit(1)

profile = profile_response.json()
print("Seller profile created:", profile)