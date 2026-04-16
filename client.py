import time, hmac, hashlib, requests
from urllib.parse import urlencode
import os
from dotenv import load_dotenv

load_dotenv()

class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.secret = os.getenv("API_SECRET")
        self.base_url = os.getenv("BASE_URL")

    def _sign(self, params):
        query = urlencode(params)
        return hmac.new(
            self.secret.encode(),
            query.encode(),
            hashlib.sha256
        ).hexdigest()

    def send_request(self, method, endpoint, params=None):
        if params is None:
            params = {}

        params["timestamp"] = int(time.time() * 1000)
        params["signature"] = self._sign(params)

        headers = {"X-MBX-APIKEY": self.api_key}
        url = self.base_url + endpoint

        try:
            if method == "POST":
                res = requests.post(url, headers=headers, params=params)
            elif method == "GET":
                res = requests.get(url, headers=headers, params=params)

            res.raise_for_status()
            return res.json()

        except Exception as e:
            raise Exception(f"API Error: {e}")