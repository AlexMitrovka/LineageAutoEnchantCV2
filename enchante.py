import threading
import json
import time
from ctypes import windll, Structure, c_long, byref
import keyboard as kbd
import logging
from time import sleep
"""Import Visiom"""
from tools.matches import VisionEnchante
"""Import all HID"""
from HID import keyboard, mouse, controller, keyboardMod

import logging
"""Create Controller"""
Key, Button = keyboardMod.Key, keyboardMod.Button
_keyboard = keyboard.Keyboard()
_mouse = mouse.Mouse()
hid = controller.ArduinoController(_keyboard, _mouse)

"""
Запис координат заточки 
GLOBAL KEY E - START|STOP,
            X - PUSH cord to list
            S - SAVE rec 
            QQ - EXIT
            
"""
"""
Global Setting
"""
HOW_MUCH = "+10" #defaul

filepos_name = 'cord.json'
pos = []
base_interval = float(0.2)
class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def get_cur_pos():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    # print(f"Add pos x:{pt.x} - y:{pt.y}")
    return {"x": pt.x, "y": pt.y}

def enchante(count):
    if not pos:
        with open(filepos_name, 'r') as file:
          pos.append(json.load(file))
    cord = pos[0]
    print(cord)
    text_vision = None
    with hid:
        while text_vision != count:

            for di in cord:
                hid.click(1, di['x'], di['y'])
                sleep(0.10)
            #print("time", time.time() - start)
            text_vision = VisionEnchante()
            print(text_vision)
def test_vision():
        start = time.time()
        text_vision = VisionEnchante()
        end = time.time()-start
        print(f"time:{end}, text:{text_vision}")

def global_key():
    isTrue = True #Flag Start / Stop while
    while isTrue:
        event = kbd.read_event() # read key event in loop
        if event.event_type == kbd.KEY_DOWN and event.name == 'e': #Start enchante
            enchante(HOW_MUCH)
            #test_vision()
        if event.event_type == kbd.KEY_DOWN and event.name == 'x': #Press to get current pos cord x, y
            pos.append(get_cur_pos()) #write positions mouse to pos dict
            print(f"pos add {get_cur_pos()}")
        if event.event_type == kbd.KEY_DOWN and event.name =='s': #save json positione
            with open(filepos_name, 'w') as file:
                json.dump(pos, file)
            print("File Save successfully")
        if event.event_type == kbd.KEY_DOWN and event.name == 'q': # Stop cycle and
            isTrue = False
            kbd.wait('q') #Wait Keypress 'q' and exit whilexs


def main():
    key_handler = threading.Thread(target=global_key)
    key_handler.start()


if __name__ == '__main__':
        main()
