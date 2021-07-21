import time
def join_meet(userdata):
    import keyboard
    
    keyboard.press_and_release('ctrl + e, ctrl + d')
    for j in range(8):
        keyboard.press_and_release('tab')
    keyboard.press_and_release('enter')
    time.sleep(2)
    for j in range(8):
        keyboard.press_and_release('tab')
    keyboard.press_and_release('enter')
    keyboard.write(userdata)
    
