import time
from HID.serialConnect import Connection
from HID.settings import Settings
from HID.keyboard import KeyboardInterface
from HID.mouse import MouseInterface

class ArduinoController:
    def __init__(self, keyboard:[KeyboardInterface], mouse:[MouseInterface]):
        self.settings = Settings()
        self.keyboard = keyboard
        self.mouse = mouse
        self.connection = Connection(self.settings.com_port, self.settings.baund_rate)


    def __enter__(self):
        print("Entering context")
        self.connection.connect(None)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        self.connection.close_connection()

    def pressKey(self, key):
         self.connection.send_command(self.mouse.mouse_press(key))

    def releaseKey(self, key):
         self.connection.send_command(self.mouse.mouse_release(key))

    def move(self, x, y):
         self.connection.send_command(self.mouse.moveTo(x, y))

    def drag_and_drop(self, x, y, xt, yt, interval=0.25, duration=None, key=1):
        self.move(x,y)
        self.pressKey(key)
        self.move(xt,yt)
        time.sleep(interval)
        self.releaseKey(key)

    def click(self, key, x=None, y=None):
        self.connection.send_command(self.mouse.click(key, x, y))

    def kbPress(self, key):
        self.connection.send_command(self.keyboard.kbdPress(key))

    def kbWrite(self, char):
        self.connection.send_command(self.keyboard.kbdWrite(char))

    def kbRelease(self, key):
        self.connection.send_command(self.keyboard.kbdRelease(key))

    def kbReleaseAll(self):
        self.connection.send_command(self.keyboard.kbdReleaseAll())

    def kbPrint(self, str):
        self.connection.send_command(self.keyboard.kbdPrint(str))


