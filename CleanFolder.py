#this script looks into specified folder
#determine today's date
#find dates of all listed file and create a dictionary
#create folders for dates in the past
#move files older than one day into respective date listed

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
        if j[0:10] == compare:
            continue
        else:
            print("move file" + onlyfiles[z])
            movedir = photopath + "\\" + j[0:10]
            movefile = photopath + "\\" + onlyfiles[z]
            shutil.move(movefile, movedir + "\\" + j)

#code reference
# import os
# import shutil

# os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
# shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
# os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

#note: os.rename care about which disk. shutil.move does not care about which disk for storage


if __name__ == '__main__': main()