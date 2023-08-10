import ctypes
from abc import ABC, abstractmethod

# class POINT(ctypes.Structure):
#     _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]



class MouseInterface(ABC):
    @abstractmethod
    def moveTo(self, x, y):
        pass

    @abstractmethod
    def click(self, key,x=None,y=None):
        pass

    @abstractmethod
    def mouse_press(self, key):
        pass

    @abstractmethod
    def mouse_release(self, key):
        pass


class Mouse(MouseInterface):
    LEFT = 1
    RIGHT = 2
    MIDDLE = 4
    def moveTo(self, x, y):
        command = f"MV{x},{y};"
        #print(command)
        return command

    def click(self, key, x=None, y=None):
        command = f"MC{key};"
        if x and y:
            return self.moveTo(x, y)+command
        else:
            return command

    def mouse_press(self, key):
        command = f"MP{key};"
        #print(command)
        return command

    def mouse_release(self, key):
        command = f"MR{key};"
        #print(command)
        return command





