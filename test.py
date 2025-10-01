import requests
from pprint import pprint
from configuration_access.config import API_KEY

def test_sncf_api():
    url = "https://api.sncf.com/v1"  
    headers = {"Authorization": API_KEY}

    response = requests.get(url, headers=headers)
    print("Status code:", response.status_code)
    pprint(response.json())

if __name__ == "__main__":
    test_sncf_api()
