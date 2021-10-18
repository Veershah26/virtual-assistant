import requests
import json

error = "The API quota is full, please try again in sometime"

def joke_api():
    try:
        joke = requests.get('https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Pun,Spooky,Christmas?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt')
        print(f"Here is your joke - \n{joke.text}")

    except Exception as e: #throws an error if the API quota is exceeded.
        print(error)

def quote():
        try:
            response = requests.get("https://zenquotes.io/api/random")
            json_data = json.loads(response.text)
            quote = json_data[0]['q'] + " Quote by - " + json_data[0]['a']
            print(f"Here is your quote - \n{quote}")

        except Exception as e: #throws an error if the API quota is exceeded.
            print(error)

def quote_of_the_day():
    try:
        response = requests.get("https://zenquotes.io/api/today")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " Quote by - " + json_data[0]['a']
        print(f"Here is the quote of the day - \n{quote}")

    except Exception as e: #throws an error if the API quota is exceeded.
        print(error)

def github():
    user = str(input("Enter the github username: ")) #Takes the username of the github user
    try:
        githubuser = requests.get(f"https://api.github.com/users/{user}") #requests the data of the github user
        github_data = json.loads(githubuser.text) 
        print(f"""Here is the github info about - {github_data['login']} - 
Name - {github_data['name']} 
Github ID - {github_data['id']}
Site Admin? - {github_data['site_admin']}
Location - {github_data['location']}
Company - {github_data['company']}
Public Repos - {github_data['public_repos']}
Public Gists - {github_data['public_gists']}
Followers - {github_data['followers']}
Following - {github_data['following']}
Joined Github At - {github_data['created_at'][:10]}
Last Activity At - {github_data['updated_at'][:10]}
""") #Extracting data from the api, and displaying it to the user
            
    except Exception as e: #throws an error, if invalid user found, or if the API quota is exceeded.
        print(error)
