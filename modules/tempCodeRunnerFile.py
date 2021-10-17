except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
	except sr.UnknownValueError:
		print("unknown error occured")