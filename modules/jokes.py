from joke.jokes import *
from random import choice
from main import *


def jokes():
    random_joke = choice([geek, icanhazdad, chucknorris, icndb])()
    # assigning random_joke variable to get random jokes.
    speak(random_joke)
    # virtual assistant narrating it.


jokes()
