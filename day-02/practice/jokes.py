import requests

api_url = "https://official-joke-api.appspot.com/random_joke"

def get_joke():
    joke = requests.get(api_url)
    #final_joke = joke.json() ["setup"] + joke.json() ["punchline"]

    if joke.status_code == 200:
        print("Your URL : ",joke.url)
        print("Status Code :", joke.status_code)
        print("\nHere's a random joke for you:\n")
        print(joke.json(), "\n")
    else:
        print("Failed to retrieve a joke. Please try again later.")
        return
    
    print("Joke Details:")
    for key, value in joke.json().items():
        print(f"{key} : {value}")

get_joke()