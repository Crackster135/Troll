import time
import sys
import random
import webbrowser

firefox_path = '/usr/bin/firefox'

def open(n):
    webbrowser.get(firefox_path).open('https://i.kym-cdn.com/entries/icons/facebook/000/040/160/smokingcaterpillarkrater.jpg')
    # while n <= random.randint(20,200):
    #     n+=1
    #     time.sleep(random.uniform(0, 0.5))