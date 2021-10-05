import time
import os
from win10toast import ToastNotifier
from random import choice

def StressBusters():
    n = ToastNotifier()

    # check for file existence so that user don't have to input each time
    flag = 1
    if os.path.exists('StressBustersSettings.txt'):
        if os.stat('StressBustersSettings.txt').st_size != 0:
            with open('StressBustersSettings.txt', 'r') as file:
                my_time = int(file.read())
                print('Frequency set to ' + str(my_time) + ' minutes.')
        else:
            flag = 0
    else:
        flag = 0

    # storing the frequency value for future use
    if not flag:
        my_time = int(input('Frequency of StressBusters Notification (in minutes): '))
        print('Frequency set to ' + str(my_time) + ' minutes.')
        with open('StressBustersSettings.txt', 'w') as file:
            file.write(str(my_time))

    tstart = round(time.time())
    # interesting messages for user to have peace
    messages = ['Have a look around!', 'Breathe IN....Breathe OUT', 'Enjoy the fresh air :)', 'One step at a time is a Good Walking',
                'Give me some rest :(', 'Close your eyes and take deep breathe.', 'Time to RelaX', 'Peace Out ✌']

    # based on the freq value set, notification pops out for the user
    while True:
        if round(time.time()) - tstart == my_time * 60:
            n.show_toast('StressBusters', choice(messages), duration=10)  # 20
            tstart = round(time.time())

StressBusters()
