from sets import Set

valid_auto_commands = Set(['takeoff','exit', 'stop'])
valid_data_commands = Set(['battery?','time?','wifi?', 'speed?'])
valid_move_commands = Set(['up', 'down', 'left', 'right', 'forward', 'back'])

class Validate:

    def command(self, command):
        valid = False
        valid_command = ''
        try:
            if command in valid_move_commands:
                print('Please enter a move distance between 20-500...')
                distance = int(raw_input())
                if 20 <= distance <= 500:
                    command += ' '
                    command += `distance`
                    valid = True
                else:
                    print('Invalid value...')
            elif command in valid_auto_commands:
                if command == 'takeoff':
                    valid_auto_commands.remove(command)
                    valid_auto_commands.add('land')
                    valid = True
                if command == 'land':
                    valid_auto_commands.remove(command)
                    valid_auto_commands.add('takeoff')
                    valid = True
            elif command in valid_data_commands:
                valid = True
            elif command == 'speed':
                print('Please enter a speed between 10-100...')
                speed = int(raw_input())
                if 10 <= speed <= 100:
                    command += ' '
                    command += `speed`
                else:
                    print('Invalid value...')
            else:
                valid = False
        except:
            valid = False
        
        valid_command = command
        return valid, valid_command
