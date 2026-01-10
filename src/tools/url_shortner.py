import requests
from src.constant import constant
API_TOKEN = ""


def shorten_url(self, long_url: str) -> str:
    """Shortens the given long URL using the TinyURL API."""
    try:
        headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json"
        }
        payload = {
            "url": long_url,
            "domain": "tinyurl.com"
        }
        response = requests.post(constant.TINYURL_API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()["data"]["tiny_url"]
        return "Failed to shorten the URL"
    except Exception as e:
        print(f"Error shortening URL: {e}")
        return "Failed to shorten the URL"
