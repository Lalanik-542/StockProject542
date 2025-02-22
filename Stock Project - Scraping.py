import requests
from bs4 import BeautifulSoup
import re
from colorama import Fore
print (Fore.LIGHTGREEN_EX)

url = "https://finance.yahoo.com/research-hub/screener/sec-ind_ind-largest-equities_biotechnology/?guccounter=1&guce_referrer=aHR0cHM6Ly9maW5hbmNlLnlhaG9vLmNvbS8&guce_referrer_sig=AQAAAAM5agQkSo4654_hfLz6Y-AcbZ-20pz2_Loz8iAo-hkVRhYWPhYhZ2-moKRORw1A6js0_NU3XT6xhNe7Ug_PjUZ6tm2BqaufH-wsXU1pF7in4nXjIiZpVXLwBq5RS0WcsPeWYMfvrCxhjfFFufhEINYpQaIIWaicJGb-OuyFF6OU"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    tickers = soup.find_all("td", class_="yf-fanlnn lpin shad")

    ticker_list = []

    if tickers:
        for ticker in tickers:
            # Extract full text, including from any nested tags
            ticker_text = "".join(ticker.stripped_strings)

            # Regex to capture alphanumeric tickers with dots, dashes, and numbers
            if re.match(r"^[A-Za-z0-9.\-]+$", ticker_text):
                ticker_list.append(ticker_text)

        if ticker_list:
            print("".join(ticker_list))
        else:
            print(Fore.RED + "No valid tickers found. Check class name or structure.")
    else:
        print(Fore.RED + "No tickers found. Please check the class name or structure.")
else:
    print(Fore.RED + f"Failed to fetch data. Status code: {response.status_code}")
