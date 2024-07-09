import time
import sys
import random
import webbrowser

firefox_path = '/usr/bin/firefox'

def open(n):
    while n <= random.randint(1,10):
        webbrowser.get(firefox_path).open('https://i.kym-cdn.com/entries/icons/facebook/000/040/160/smokingcaterpillarkrater.jpg')
        n+=1
        time.sleep(random.uniform(0, 0.5))