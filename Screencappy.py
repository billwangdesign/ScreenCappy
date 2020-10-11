import pyautogui
from datetime import datetime
import time
from datetime import date
import os
from time import sleep


def main():
    #create variable pointing to target directory for saving pictures
    path = os.environ['USERPROFILE']
    photopath = path + "\\Pictures\\ScreenCappy"

    #if ScreenCappy folder does not exist, create folder
    if not os.path.exists(photopath):
        os.makedirs(photopath)

    #continously take screen shot of screen and save it to directory in "photopath" variable
    while True:
        now = datetime.now()
        filename = now.strftime("%Y-%m-%d_%H-%M-%S.png")
        fullname = photopath + "\\" + filename
        pyautogui.screenshot(fullname) 
        time.sleep(30)


if __name__ == '__main__': main()