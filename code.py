import board
import digitalio
import time

left_pins = [
    digitalio.DigitalInOut(board.GP0),
    digitalio.DigitalInOut(board.GP1),
    digitalio.DigitalInOut(board.GP2),
    digitalio.DigitalInOut(board.GP3),
    digitalio.DigitalInOut(board.GP4),
    digitalio.DigitalInOut(board.GP5),
    digitalio.DigitalInOut(board.GP6),
    digitalio.DigitalInOut(board.GP7),
    digitalio.DigitalInOut(board.GP8),
    digitalio.DigitalInOut(board.GP9),
    digitalio.DigitalInOut(board.GP10),
    digitalio.DigitalInOut(board.GP11),
    digitalio.DigitalInOut(board.GP12),
    digitalio.DigitalInOut(board.GP13),
    digitalio.DigitalInOut(board.GP14),
    digitalio.DigitalInOut(board.GP27)
]
right_pins = [
    digitalio.DigitalInOut(board.GP16),
    digitalio.DigitalInOut(board.GP17),
    digitalio.DigitalInOut(board.GP18),
    digitalio.DigitalInOut(board.GP19),
    digitalio.DigitalInOut(board.GP20),
    digitalio.DigitalInOut(board.GP21),
    digitalio.DigitalInOut(board.GP22),
    digitalio.DigitalInOut(board.GP26)
]

keys = [
    "ESC","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","PAUSE","PrtScr","Ins","Del",
    "GRAVE","1","2","3","4","5","6","7","8","9","0","-","=","BkSp",
    "TAB","Q","W","E","R","T","Y","U","I","O","P","[","]","Backslash",
    "CAPS","A","S","D","F","G","H","J","K","L",";","QUOTE","ENTER",
    "L-SHIFT","Z","X","C","V","B","N","M","<",">","?","R-SHIFT",
    "Fn","L-CTRL","L-WIN","L-ALT","SPACE","R-ALT","MENU","HOME","UP","END","PGUP",
    "R-WIN","LEFT","DOWN","RIGHT","PGDN"
]
print("Starting scan:")
for key in keys:
    print(key)
    time.sleep(1)
    found = False
    while found==False:
        for out_index, out_pin in enumerate(left_pins):
            out_pin.direction = digitalio.Direction.OUTPUT
            out_pin.value = True
            time.sleep(0.001)
            for in_index, in_pin in enumerate(right_pins):
                in_pin.switch_to_input(pull=digitalio.Pull.DOWN)
                time.sleep(0.001)
                if(in_pin.value):
                    print (key, out_index, in_index)
                    found = True
                    time.sleep(0.5)
                    break
            out_pin.value = False

    


