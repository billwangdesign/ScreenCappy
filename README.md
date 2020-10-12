# ScreenCappy
Screencapture and Organization for time lapse

This project consists of two files
1. Screen capture - take a screenshot of primary screen every 30 seconds. Save screen captures at specified user folder. It does not capture secondary screen if there are more than one screen. 

2. Folder organization - create a folder for each day that screen cappy has ran. This program does not move file created today but moves files in all other days in its respective folder. 

A single .exe file is created for eacy .py 

To setup, run task scheduler
    File                    Trigger
    Screencappy.exe         At log on
    Screencappy.exe         On Workstation unlock of any user
    Clean Screencappy.exe   Daily 8AM (change time as required)