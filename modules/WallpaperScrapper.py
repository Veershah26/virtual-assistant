import os
import shutil
import getpass as gp
import tkinter
from tkinter.filedialog import askdirectory

def WallpaperScrapper():
    username = gp.getuser()
    path = os.path.join(r'C:\Users', username) + r'\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
    tkinter.Tk().withdraw()
    target_path = askdirectory(title='Select Folder')

    if target_path:
        for file in os.listdir(path):
            original = os.path.join(path, file)
            target = os.path.join(target_path, file + '.jpg')
            shutil.copyfile(original, target)
        print('Wallpapers copied to desired location successfully!!')
    else:
        print('Invalid username or folder location!!')

if __name__ == '__main__':
    WallpaperScrapper()
