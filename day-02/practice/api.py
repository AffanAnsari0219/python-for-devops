import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

print("Your URL : ",response.url)
print("Status Code :", response, "\n")

#print(dir(response), "\n")
print(response.json(), "\n")

for key,value in response.json().items():
    print(key, ":", value)
    if key == "completed":
        if value:
            print("The TODO is completed")
        else:
            print("The TODO is not completed")