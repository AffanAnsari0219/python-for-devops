import requests  # type: ignore
import json

API_KEY = "TCBY95O2XXPWFAQ1"
API_URL = "https://www.alphavantage.co/"

def get_stock_market_data(api_symbol):
    try:
        api_function = "TIME_SERIES_DAILY"
        api_query = f"query?function={api_function}&symbol={api_symbol}&apikey={API_KEY}"

        response = requests.get(API_URL + api_query, timeout=10)

        print("Your URL :", response.url)
        print("Your URL Response Code is :", response.status_code, "\n")

        response.raise_for_status()

        data = response.json()

        processed_data = {}

        for key, value in data.items():
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

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again later.")

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the API. Check your internet connection.")

    except requests.exceptions.HTTPError:
        print("Error: HTTP error occurred while calling the API.")

    except json.JSONDecodeError:
        print("Error: Failed to parse API response (Invalid JSON).")

    except Exception as error:
        print("Unexpected error occurred:", error)

api_symbol = input("Enter the stock market symbol (e.g., AMZN, AAPL, IBM, GOGL) : ")
get_stock_market_data(api_symbol)