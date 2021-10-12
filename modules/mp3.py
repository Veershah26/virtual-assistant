#Import modules that is required by this program
from playsound import playsound
from tkinter import Tk, filedialog

# Creating a dialog box to select music
root = Tk()
root.withdraw()
root.attributes('-topmost', True) 

# Function to play music that user choose
def playmusic():
    repeat=1
    print("Select your music")
    open_file = filedialog.askopenfilename()
    #loop asking for repeat or exit 
    while(repeat):
        print('Playing your music........')
        playsound(open_file)
        res=int(input('Do you want to play again..Enter 1 for yes and 0 for No'))
        if (res==1):
            repeat=1
        elif res==0:
            repeat=0
        else:
            print('You entered wrong input..so Exit')
            repeat=0

if __name__ == "__main__":
    playmusic()