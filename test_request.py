# test_request.py
import requests
import json

url = "http://127.0.0.1:5000/predict"

payload = {
    "fever": 1,
    "vomiting": 1,
    "headache": 2

}


try:
    resp = requests.post(url, json=payload, timeout=5)
    resp.raise_for_status()
    print("Status code:", resp.status_code)
    print("Response JSON:")
    print(json.dumps(resp.json(), indent=2))
except requests.exceptions.ConnectionError:
    print("Connection error: Is your Flask app running? Run: python app.py")
except requests.exceptions.Timeout:
    print("Request timed out.")
except Exception as e:
    print("Error:", str(e))
