

class FreeMode():

    def __init__(self, tello):
        self.tello = tello

    def free_mode(self):

        while True:
            print('Please enter a command...')
            try:
                command = raw_input().rstrip().lower()
                if command == 'exit':
                    break
                self.tello.send_command(command)
            except:
                print('invalid command...')