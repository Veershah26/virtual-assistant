import requests
import json

error = "The API quota is full, please try again in sometime"

def api():
    user = str(input("How may I help you?: "))
    if user == "tell me a joke":
        try:
            joke = requests.get('https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Pun,Spooky,Christmas?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt')
            print(f"Here is your joke - \n{joke.text}")

        except Exception as e:
            print(error)

    if user == "tell me a quote":
        try:
            response = requests.get("https://zenquotes.io/api/random")
            json_data = json.loads(response.text)
            quote = json_data[0]['q'] + " Quote by - " + json_data[0]['a']
            print(f"Here is your quote - \n{quote}")

        except Exception as e:
            print(error)

    if user == "what is the quote of the day" or user == "quote of the day":
        try:
            response = requests.get("https://zenquotes.io/api/today")
            json_data = json.loads(response.text)
            quote = json_data[0]['q'] + " Quote by - " + json_data[0]['a']
            print(f"Here is the quote of the day - \n{quote}")

        except Exception as e:
            print(error)

api()
