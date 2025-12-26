import requests  # type: ignore
import json

API_KEY = "TCBY95O2XXPWFAQ1"
api_url = "https://www.alphavantage.co/"

def get_stock_market_data(api_symbol):
    api_function = "TIME_SERIES_DAILY"
    api_query = f"query?function={api_function}&symbol={api_symbol}&apikey={API_KEY}"
    response = requests.get(api_url + api_query)

    print("Your URL :", response.url)
    print("Your URL Response Code is :", response.status_code, "\n")

    processed_data = {}

    for key, value in response.json().items():
        if key == "Meta Data":
            processed_data["Meta Data"] = value
            print("Meta Data:")
            for meta_key, meta_value in value.items():
                print(f"{meta_key} : {meta_value}")

        if key == "Time Series (Daily)":
            processed_data["Time Series (Daily)"] = {}
            print("\nDaily Time Series Data:")

            for date, daily_data in value.items():
                print(f"Date: {date}")
                processed_data["Time Series (Daily)"][date] = daily_data

                for data_key, data_value in daily_data.items():
                    print(f"  {data_key} : {data_value}")
                print()
                break

    file_name = f"{api_symbol}_stock_data.json"
    with open(file_name, "w") as json_file:
        json.dump(processed_data, json_file, indent=4)

    print(f"Stock data saved successfully to {file_name}")

    return response

api_symbol = input("Enter the stock market symbol (e.g., AMZN, AAPL, IBM, GOGL) : ")
get_stock_market_data(api_symbol)