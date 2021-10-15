import requests
import json

'''
1. The function takes in no arguments.
2. The function then tries to get a quote from the REST- Api
3. If the REST- Api is not available, then the function returns None.
4. If the REST- Api is available, then the function returns a quote from the REST- Api.
'''

def random_quote():
    try:
        response=requests.get("https://efflux.herokuapp.com/random")
        json_data=json.loads(response.text)
        quote =json_data['q'] + " by "+json_data["a"]
        return quote
    except:
        pass

def business_quote():
    try:
        response=requests.get("https://efflux.herokuapp.com/business")
        json_data=json.loads(response.text)
        quote =json_data['q'] + " by "+json_data["a"]
        return quote
    except:
        pass

def love_quote():
    try:
        response=requests.get("https://efflux.herokuapp.com/love")
        json_data=json.loads(response.text)
        quote =json_data['q'] + " by "+json_data["a"]
        return quote
    except:
        pass

def hustle_quote():
    try:
        response=requests.get("https://efflux.herokuapp.com/hustle")
        json_data=json.loads(response.text)
        quote =json_data['q'] + " by "+json_data["a"]
        return quote
    except:
        pass

def life_quote():
    try:
        response=requests.get("https://efflux.herokuapp.com/life")
        json_data=json.loads(response.text)
        quote =json_data['q'] + " by "+json_data["a"]
        return quote
    except:
        pass

def friendship_quote():
    try:
        response=requests.get("https://efflux.herokuapp.com/friendship")
        json_data=json.loads(response.text)
        quote =json_data['q'] + " by "+json_data["a"]
        return quote
    except:
        pass

def war_quote():
    try:
        response=requests.get("https://efflux.herokuapp.com/war")
        json_data=json.loads(response.text)
        quote =json_data['q'] + " by "+json_data["a"]
        return quote
    except:
        pass

def game_quote():
    try:
        response=requests.get("https://videogame-quotes-api.herokuapp.com/quotes")
        json_data=json.loads(response.text)
        quote =json_data['quote'] + " from "+json_data["game"]
        return quote
    except:
        pass

#print(random_quote())    # EXAMPLE 