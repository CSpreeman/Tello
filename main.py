import sys
import time
from tello import Tello
from datetime import datetime
from command_mode import CommandMode
from free_mode import FreeMode
from tello_state import TelloState

start_time = time.strftime("%Y%m%d-%H%M%S")
tello = Tello()
tello.send_command_await('command')

while True:
    print('Available Modes: Free, Command')
    print('Mode?....')
    mode = raw_input().rstrip().lower()

    try:
        if mode == 'free':
            print('Entered free mode')
            tello.print_thread_response = False
            mode = FreeMode(tello)
            mode.free_mode()
        elif mode == 'command':
            print('Entered command mode')
            mode = CommandMode(tello)
            mode.command_mode()
        elif mode == 'exit':
            break
    except:
        print('Invalid Command....')


log = tello.get_log()
out = open('C:/Users/Craig/Desktop/Tello-master/log/' + start_time + '.txt', 'w')
for stat in log:
    stat.print_stats()
    str = stat.return_stats()
    out.write(str)