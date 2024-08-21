import subprocess
import threading
import random

firefox_path = '/usr/bin/firefox'

with open('events/media/data/urls.txt', 'r') as file:
    urls = file.readlines()

def open_firefox_window():
    subprocess.Popen([firefox_path, urls[random.randint(0, len(urls) - 1)]])

def open_multiple_windows(n):
    threads = []
    for _ in range(n):
        t = threading.Thread(target=open_firefox_window)
        t.start()
        threads.append(t)
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
