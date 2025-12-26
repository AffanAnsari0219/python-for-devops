import requests

API_KEY = "TCBY95O2XXPWFAQ1"
api_url = "https://www.alphavantage.co/"

def get_stock_market_data(api_symbol):
    api_function = "TIME_SERIES_DAILY"
    api_query = f"query?function={api_function}&symbol={api_symbol}&apikey={API_KEY}"
    response = requests.get(api_url + api_query)

    print("Your URL :", response.url)
    print("Your URL Response Code is :", response.status_code, "\n")

    for key, value in response.json().items():
        if key == "Meta Data":
            print("Meta Data:")
            for meta_key, meta_value in value.items():
                print(f"{meta_key} : {meta_value}")
        if key == "Time Series (Daily)":
            print("\nDaily Time Series Data:")
            for date, daily_data in value.items():
                print(f"Date: {date}")
                for data_key, data_value in daily_data.items():
                    print(f"  {data_key} : {data_value}")
                print()
                break
    return response

api_symbol = input("Enter the stock market symbol (e.g., AMZN, AAPL, IBM, GOGL) : ")
get_stock_market_data(api_symbol)