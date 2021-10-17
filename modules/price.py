import requests
from bs4 import BeautifulSoup

'''
1. The function takes in one argument: url, the URL to be searched
2. The function then makes a request to the URL and gets the HTML content
3. The function then uses BeautifulSoup to parse the HTML content
4. The function then finds the div with the class "BNeawe iBp4i AP7W"
'''

def price(coin):
    try:
        coin=coin.lower()
        url=f'https://www.google.com/search?q={coin}+price'
        HTML=requests.get(url)
        soup=BeautifulSoup(HTML.text,'html.parser')
        text=soup.find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
        return text
    except:
        return "Not found"


#print(price('bitcoin'))         #Example
#print(price('litecoin'))        #Example