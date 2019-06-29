from validate_command import Validate

class CommandMode:

    def __init__(self, tello):
        self.tello = tello
    
    def command_mode(self):
        validate = Validate()

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
                else:
                    valid, valid_command = validate.command(command, ext)
            except:
                valid = False


            if valid:
                print('Valid ' + valid_command)
                self.tello.send_command(valid_command)
            else:
                print('Invalid Command...')
