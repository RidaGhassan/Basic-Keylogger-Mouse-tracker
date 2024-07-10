from pynput.mouse import Controller
from pynput.keyboard import Controller

# You cannot simultaneously control the mouse and the keyboard.
# ( left to right, top to bottom )
# Top-left of the screen is (0,0)
def Mousecontrol():
    mouse = Controller()
    mouse.position = (720,540)

def controlkeyboard():
     keyboard = Controller()
     keyboard.type(" I can type without typing!")

controlkeyboard()

# Mouse control using Python
# I can type without typing!
# I can type without typing!