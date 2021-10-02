  
import pyscreenshot
import datetime
  
image = pyscreenshot.grab()
image.show()
a = datetime.datetime.now()
image.save(f"{a.day,a.month,a.year}.png")
