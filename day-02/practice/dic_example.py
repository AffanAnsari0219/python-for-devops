"""
info = {
    "name": "Mohammed Affan Ansari",
    "email": "affanansari12@gmail.com",
    "phone": "+91-7977406645",
    "favorite_languages": ["Python", "JavaScript", "C++"]
}

print("My name is :", info["name"])
print("My favourite languages are :", info["favorite_languages"])
print("Total favorite languages listed are :", len(info["favorite_languages"]))
info["favorite_languages"].append("Java")
print("Updated favorite languages are :", info["favorite_languages"])

info["country"] = "India"
print("My country is :", info["country"])
"""




info = {
    "name" : "Mohammed Affan Ansari",
    "country" : "India",
    "married" : True,
    "age" : 27,
    "salary" : 65000.50,
    "fav" : ["books", 12, 0.2, False]
}

print("My name is :", info["name"])
print("I live in :", info.get("county", "Not Specified"))
info.update({"email" : "affanansari12@gmail.com"})
print("My email is :", info["email"], "\n")


print(info)
print(info.keys())
print(info.values(), "\n")

for key,value in info.items():
    print(f"{key} : {value}")