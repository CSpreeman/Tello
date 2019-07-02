import socket
import threading

class TelloState:

    def __init__(self):
        self.local_ip = ''
        self.local_port = 8890
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket for sending cmd
        self.socket.bind((self.local_ip, self.local_port))

        # thread for receiving cmd back
        self.receive_thread = threading.Thread(target=self._receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()

    def _receive_thread(self):
        while True:
            try:
                self.response, ip = self.socket.recvfrom(1024)
                print('State From %s: %s' % (ip, self.response))
            except socket.error, exc:
                print "Caught exception socket.error : %s" % exc