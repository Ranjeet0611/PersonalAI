import requests

AVIATION_STACK_API_KEY = ""


def get_flight_status(flight_number):
    """Fetches the flight status for the given flight number using the Aviation Stack API.
    The flight number should be a string, e.g., "6E6039".
    Example user query: "What is the status of flight 6E6039?"
    """
    try:
        url = "https://api.aviationstack.com/v1/flights"
        params = {
            "access_key": AVIATION_STACK_API_KEY,
            "flight_iata": flight_number,
            "limit": 1
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json().get("data", [])
        if not data:
            return "No flight data found for today"
        return data[0]
    except Exception as e:
        print(f"Error fetching flight status: {e}")
        return "No flight data found for today"
