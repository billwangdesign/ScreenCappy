from datetime import datetime
import time
from datetime import date
import os
from os.path import isfile, join
from os import listdir
import shutil

def main():
    path = os.environ['USERPROFILE']
    photopath = path + "\\Pictures\\ScreenCappy"
    
    #list of files save in onlyfiles as a list
    onlyfiles = [f for f in listdir(photopath) if isfile(join(photopath, f))]

    datelist = []

    #for every file, extract only dates, save to datelist
    for x in range(0, len(onlyfiles)):
        k = onlyfiles[x]
        datelist.append(k[0:10])

    #create list of unique dates
    uniquedate = list(set(datelist))

    #create folder for every unique date if it doesn't exist already
    for y in range(0, len(uniquedate)):
       if not os.path.exists(photopath + "\\" + uniquedate[y]):
           os.makedirs(photopath + "\\" + uniquedate[y])

    #set compare to today's date
    now = datetime.now()
    compare = now.strftime("%Y-%m-%d")

    #if it's not today, move files into folders matching other dates
    for z in range(0, len(onlyfiles)):
        j = onlyfiles[z]
        if j[0:10] == compare: #if file is today, skip to next file
            continue
        else: #if file is not today, move file to corresponding folder by date
            print("move file" + onlyfiles[z])
            movedir = photopath + "\\" + j[0:10]
            movefile = photopath + "\\" + onlyfiles[z]
            shutil.move(movefile, movedir + "\\" + j)

if __name__ == '__main__': main()