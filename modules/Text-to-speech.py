# Import the Gtts module for text
# to speech conversion
from gtts import gTTS

# import Os module to start the audio file
import os

mytext = 'Hello this sentence is converted to speech by Hardik Raval..'

# Language we want to use
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("output.mp3")

# Play the converted file
os.system("start output.mp3")