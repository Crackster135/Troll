import random
import string
import pyautogui
import time

random_letter = random.choice(string.ascii_lowercase)


def gibberish(count):
    gibberish_text = ""
    while count > 0:
        gibberish_text += random.choice(string.ascii_lowercase)
        count -= 1
        pyautogui.write(gibberish_text, interval=0.001)

