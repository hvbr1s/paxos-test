import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
SELLER_PROFILE = '283fe603-67f1-4d01-bd13-0fa486203ff4'

def get_auth_token():
    # get 0auth token for  transfer
    token_url = "https://oauth.sandbox.paxos.com/oauth2/token"
    token_response = requests.post(
        token_url, 
        data={
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "scope": "funding:read_profile funding:write_profile transfer:read_transfer transfer:write_crypto_withdrawal transfer:write_deposit_address",
            }
        )

    if token_response.status_code != 200:
        print("Auth failed:", token_response.status_code, token_response.text)
        exit(1)

    access_token = token_response.json()["access_token"]
    print("Authenticated successfully")
    print(f"Token: {access_token}")
    
    return access_token
