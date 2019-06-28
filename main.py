from tello import Tello
import sys
from datetime import datetime
from validate_command import Validate
import time

start_time = time.strftime("%Y%m%d-%H%M%S")
validate = Validate()
#tello = Tello()
#tello.send_command('command')

while True:
    print('Please enter a command...')
    valid = False
    ext = None
    command = None
    try:
        command = raw_input().rstrip().lower()
        if ' ' in command:
            command, ext = command.split(' ')
            ext = int(ext)

        if command == 'exit':
            break
        valid, valid_command = validate.command(command, ext)
    except:
        valid = False


    if valid:
        print('Valid ' + valid_command)
        #tello.send_command(valid_command)
    else:
        print('Invalid Command...')

#log = tello.get_log()
#out = open('C:/Users/Craig/Desktop/Tello-master/log/' + start_time + '.txt', 'w')
#for stat in log:
#    stat.print_stats()
#    str = stat.return_stats()
#    out.write(str)


