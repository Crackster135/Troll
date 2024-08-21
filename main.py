import random
import pyautogui, sys
import events
import time

import events.browser_events
import events.click_events
import events.image_events
import events.sound_events
import events.typing_events

print('Press Ctrl-C to quit.')
events.volume.set_volume(100)
def countdown(n):
    while n >= 1:
        print(f"Time remaining: {n} second(s)")
        time.sleep(1)
        n -= 1
    execute_function()

def execute_function():
    print("Executing function...")
    # time.sleep(random.randint(1, ))
    # events.click_events.click(3)
    # events.browser.open(1)
    # events.image_events.display_multiple_images()
    # events.typing.gibberish(40)
    # events.browser_events.open_multiple_windows(2)
    # events.sound_events.play_random_sounds(2)
    
    while True:
        chance = random.randint(1, 5)
        
        if chance == 1:
            print('browser')
            # events.browser_events.open_multiple_windows(random.randint(2, 5))
            time.sleep(random.randint(10, 20))
        elif chance == 2:
            print('click')
            # events.click_events.click(random.randint(10, 50))
            time.sleep(random.randint(10, 20))
        elif chance == 3:
            print('pic')
            doublechance = random.randint(0, 1)
            if doublechance == 0:
                print('pics')
                # events.image_events.display_multiple_images()
            else:
                print('pic')
                # events.image_events.display_image_in_window()
            time.sleep(random.randint(10, 20))
        elif chance == 4:
            print('sounds')
            # events.sound_events.play_random_sounds(random.randint(1, 5))
            time.sleep(random.randint(10, 20))
        else:
            print('typing')
            # events.typing_events.gibberish(random.randint(10, 50))
            time.sleep(random.randint(10, 20))
# Start the countdown from 
countdown(3)