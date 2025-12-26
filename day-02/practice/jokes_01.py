import requests

mood = input("What type of joke would you like to hear? (pj for random joke / dad for dad joke): ")

if mood == "pj":
    def pj_joke():
        random_joke_url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(random_joke_url)
        final_joke = response.json() ["setup"] + response.json() ["punchline"]
        return final_joke
    final_joke = pj_joke()
    print("Here's a random joke for you:\n", final_joke)
elif mood == "dad":
    def dad_joke():
        dad_joke_url = "https://icanhazdadjoke.com/"
        headers = {"Accept": "application/json"}
        response = requests.get(dad_joke_url, headers=headers)
        final_joke = response.json() ["joke"]
        return final_joke
    final_joke = dad_joke()
    print("Here's a dad joke for you:\n", final_joke)
else:
    print("Sorry, I can only tell 'pj' (random) or 'dad' jokes right now.")

'''
def dad_joke():
    headers = {"Accept": "application/json"}
    response = requests.get(dad_joke_url, headers=headers)
    final_joke = response.json() ["joke"]
    return final_joke

final_joke = dad_joke()
print("Here's a dad joke for you:\n", final_joke)
'''