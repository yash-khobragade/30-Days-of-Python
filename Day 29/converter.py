import requests

API_KEY = "9981b09350b8dbf97aa60e3f"

def fetch_conversion_rate(base_currency: str, target_currency: str) -> float:
    try:
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency.upper()}"
        response = requests.get(url)
        data = response.json()

        if data.get("result") != "success":
            raise RuntimeError("API Error: " + data.get("error-type", "Unknown error"))

        rate = data["conversion_rates"].get(target_currency.upper())
        if not rate:
            raise ValueError("Invalid target currency")
        return rate

    except Exception as e:
        raise RuntimeError(f"Failed to fetch exchange rate: {e}")


def load_currency_list(file_path=r"C:\Users\HP\Desktop\IDC Python 30 Day Challenge\Python\Day 29\currencies.txt") -> list:
    with open(file_path, "r") as file:
        return [line.strip().upper() for line in file.readlines()]
