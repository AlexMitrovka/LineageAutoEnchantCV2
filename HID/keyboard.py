from abc import ABC, abstractmethod

class KeyboardInterface(ABC):
    @abstractmethod
    def kbdReleaseAll(self):
        pass

    @abstractmethod
    def kbdRelease(self, key):
        pass

    @abstractmethod
    def kbdPress(self, key):
        pass

    @abstractmethod
    def kbdWrite(self, char):
        pass

    @abstractmethod
    def kbdPrint(self, String):
        pass


class Keyboard(KeyboardInterface):

    def kbdReleaseAll(self):
        return f"R;"

    def kbdRelease(self, key):
        return f"KR{key};"

    def kbdPress(self, key):
        return f"KP{key};"

    def kbdWrite(self, char):
        if type(char) is str:
            return f"KW{ord(char)};"
        else:
            return f"KW{char};"

    def kbdPrint(self, str):
        return f"KT{str};"


