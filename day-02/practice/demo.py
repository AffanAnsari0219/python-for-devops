import requests
import json

API_KEY = "TCBY95O2XXPWFAQ1"
api_url = "https://www.alphavantage.co/"

def get_stock_market_data(api_symbol):
    # Step 1: Define the API function
    api_function = "TIME_SERIES_DAILY"

    # Step 2: Build the API URL
    api_query = f"query?function={api_function}&symbol={api_symbol}&apikey={API_KEY}"
    full_url = api_url + api_query

    # Step 3: Send GET request to the API
    response = requests.get(full_url)

    # Step 4: Check if API call was successful
    if response.status_code != 200:
        print("❌ API request failed")
        print("Status Code:", response.status_code)
        return

    print("✅ API request successful")
    print("Your URL :", response.url)
    print("Response Code :", response.status_code, "\n")

    # Step 5: Convert API response to JSON
    data = response.json()

    processed_data = {}

    # Step 6: Read and process the JSON data
    for key, value in data.items():

        # Meta information
        if key == "Meta Data":
            print("Meta Data:")
            processed_data["Meta Data"] = value
            for meta_key, meta_value in value.items():
                print(f"{meta_key} : {meta_value}")

        # Daily stock data
        if key == "Time Series (Daily)":
            print("\nDaily Time Series Data:")
            processed_data["Time Series (Daily)"] = {}

            for date, daily_data in value.items():
                print(f"Date: {date}")
                processed_data["Time Series (Daily)"][date] = daily_data

                for price_type, price_value in daily_data.items():
                    print(f"  {price_type} : {price_value}")
                print()
                break  # Remove this to save all dates

    # Step 7: Save the processed data to a JSON file
    file_name = f"{api_symbol}_stock_data.json"
    with open(file_name, "w") as json_file:
        json.dump(processed_data, json_file, indent=4)

    print(f"📁 Stock data saved successfully in {file_name}")

# Step 8: Take user input and run the function
api_symbol = input("Enter stock symbol (AAPL, AMZN, IBM, etc.): ")
get_stock_market_data(api_symbol)
