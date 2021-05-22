from datetime import datetime
import webbrowser
import time
import random
import linecache
import os
from subprocess import Popen
import pyautogui

br = 0  # used for closing browser

for i in range(31):
    
    # random seconds waited before closing brower
    rClose = random.randint(5,20)
    
    # random seconds before we search for the next word or phrase
    rSearch = random.randint(1,18)

    # used to pick a random word from your file
    #      random.randint(first_line,last_line)
    rNum = random.randint(1,210000)
    
    # opens default brower and a random line from your file containing words
    webbrowser.open('www.bing.com/search?q=' + linecache.getline('ques.txt',rNum))
    
    # time waited before searching again
    time.sleep(rSearch)
    
    # used to find out how much tabs are opened
    br = i%5

    if br==0:    # closes browser after 5 tabes
        time.sleep(rClose)
        
        # forces brower to close
        os.system('taskkill /im chrome.exe /f')
        # os.system('taskkill /im msedge.exe /f')
        # os.system('taskkill /im iexplore.exe /f')
        




    
