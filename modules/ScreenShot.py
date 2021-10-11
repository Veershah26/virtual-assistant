import pyscreenshot
import datetime


def takescreenshot():
    image = pyscreenshot.grab()
    image.show()
    a = datetime.datetime.now()
    image.save(f"{a.day,a.month,a.year}.png")


if __name__ == "__main__":
    takescreenshot()