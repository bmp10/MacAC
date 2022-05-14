try:
    import pynput
except:
    import os
    os.system('pip3 install pynput')
    
    import pynput
    
from time import sleep

click = False

mouse = pynput.mouse.Controller()

def keydown(key):
    global click

    try:
        key = key.char
    except:
        fill = ''

    if key == 'z' or key == 'Z':
        click = not click

pynput.keyboard.Listener(on_press = keydown).start()

while True:
    if click:
        mouse.click(pynput.mouse.Button.left)
        
        sleep(0.1)
