import requests

latitude = 36.7201600
longitude = -4.4203400

api_url = "https://api.sunrise-sunset.org/"
api_query = f"json?lat={latitude}&lng={longitude}"
url = api_url + api_query

response = requests.get(url)
#print(response.json())

for key, value in response.json().items():
    if key == "results":
        print("\nSunrise and Sunset Data:")
        for data_key, data_value in value.items():
            print(f"{data_key} : {data_value}")

print(input("Enter the latitude and longitude to get sunrise and sunset times.\n"))








'''
print("To get the sunrise and sunset times.")
latitude = input("Enter latitude: ")
longitude = input("Enter longitude: ")
'''