import serial
import time

class Connection:

    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.connection = None

    @property
    def receive_data(self):
        return self.connection.read(size=1)

    def connect(self,data):
        try:
            self.connection = serial.Serial(self.port, self.baudrate, timeout=None)
            if self.connection.is_open:
                print(f"Connected to {self.port}")
        except Exception as e:
            print(f"Connection failed on port {self.port}: {e}")
            raise e

    def close_connection(self):
        self.connection.close()

    def send_command(self, command):
        self.connection.write(command.encode())
        data = self.receive_data
        if ord(data):
            pass
        else:
            raise Exception("bad send command")



