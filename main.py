import pyautogui, sys
import events
import time

print('Press Ctrl-C to quit.')

def countdown(n):
    while n >= 1:
        print(f"Time remaining: {n} second(s)")
        time.sleep(1)
        n -= 1
    execute_function()

def execute_function():
    print("Executing function...")
    events.ran_clicks.click()
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

# Start the countdown from 10
countdown(10)