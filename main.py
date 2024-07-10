import random
import pyautogui, sys
import events
import time

import events.image

print('Press Ctrl-C to quit.')

def countdown(n):
    while n >= 1:
        print(f"Time remaining: {n} second(s)")
        time.sleep(1)
        n -= 1
    execute_function()

def execute_function():
    print("Executing function...")
    # time.sleep(random.randint(1, ))
    # events.clicks.click(0)
    # events.browser.open(1)
    events.image.display_multiple_images()
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

# Start the countdown from 10
countdown(3)