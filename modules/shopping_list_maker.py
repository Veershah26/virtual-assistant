#load libraries
import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()

# function to convert text_to_speech
def text_to_speech(command):
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()

# function to take command 
def take_command():
	#data to make list
	dir_list={"Item":[],"Quantity":[]}
	try:
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source, duration=0.2)
			# Initial wishing
			text_to_speech("Hello user. You can make your shopping list here")
			text_to_speech("Do you want to make it now? Say yes or no")
			audio = r.listen(source)
			response = r.recognize_google(audio)
			response = response.lower()
			print(response)
			if response=="yes":
				text_to_speech("okk then. Lets get started")
				while(True):
					text_to_speech("say me item")
					audio2 = r.listen(source)
					MyText=r.recognize_google(audio2)
					
					MyText = MyText.lower()
					#if your list finishes:
					if MyText=="exit":
						text_to_speech("Here is your list")
						print(dir_list)

						# if list is empty it speak that list is empty
						if len(dir_list)==0:
							text_to_speech("List empty")
							return
						else:
							for i in range(len(dir_list)):
								text_to_speech(dir_list["Item"][i]+ "     "+dir_list["Quantity"][i]+"in the list")
							return
					dir_list["Item"].append(MyText)

					text_to_speech("tell me quantity")
					audio2 = r.listen(source)
					MyText = r.recognize_google(audio2)
					MyText = MyText.lower()
					dir_list["Quantity"].append(MyText)

					
			else:
				text_to_speech("Okk. So I exit.")	
	# if any wrong command given
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
	except sr.UnknownValueError:
		print("unknown error occured")


if __name__=="__main__":
	take_command()
