import os
import requests
from dotenv import load_dotenv

load_dotenv()

PAXOS_API_KEY = os.getenv("PAXOS_API_KEY")

url = "https://api.paxos.com/v2/orchestration/rules"

payload = {
    "ref_id": "my-rule-001",
    "nickname": "ETH to USD conversion",
    "profile_id": "aaa6abc4-d77a-4b81-a44d-62b17f8211f5",
    "source_asset": "PYUSD",
    "destination_asset": "USDC",
    "source": { "crypto": { "network": "ETHEREUM" } },
    "destination": { "profile": { "profile_id": "e8ea8b1c-4e8d-4c59-9e7a-c985194ba2e8" } }
}
headers = {
    f"Authorization": "Bearer {PAXOS_API_KEY}",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)