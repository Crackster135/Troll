import random
import pyautogui, sys
import events
import time

import events.browser_events
import events.click_events
import events.image_events
import events.sound_events
import events.typing_events

# 580 1552
# 250 900


print('Press Ctrl-C to quit.')
def countdown(n):
    while n >= 1:
        print(f"Time remaining: {n} second(s)")
        time.sleep(1)
        n -= 1
    execute_function()

def execute_function():
    count = 0
    try:
        while count < 20:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            x_coord = random.randint(380, 1310)
            y_coord = random.randint(300, 910)
            pyautogui.dragTo(x_coord, y_coord)
            pyautogui.click(button='left', clicks=2)
            count += 1
            print(str(x_coord) + " " + str(y_coord))
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

# Start the countdown from 
countdown(3)