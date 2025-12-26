import requests

api_url = "https://haveibeenpwned.com/"
api_query = "api/v2/breaches"

response = requests.get(api_url + api_query)

print("Your URL : ",response.url)
print("Status Code :", response.status_code, "\n")
#print(response.json(), "\n")
for breach in response.json():
    print("Breach Name :", breach["Name"])
    print("Domain     :", breach["Domain"])
    print("Breach Date:", breach["BreachDate"])
    print("Added Date :", breach["AddedDate"])
    print("Pwn Count  :", breach["PwnCount"])
    print("\nData Classes Compromised:")
    for data_class in breach["DataClasses"]:
        print(" -", data_class)
    print("\n---------------------------------\n")
