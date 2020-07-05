import time
import datetime
from tqdm import tqdm
import os
import subprocess
import pathlib
from playsound import playsound
import sys

def checkday(): #Check if current day is already in weeklylog
    currentday = datetime.datetime.today().weekday()
    daysoftheweek = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    with open("weekly.log") as f:
        datafile = f.readlines()
    for line in datafile:
        if daysoftheweek[currentday] in line:
            return True
    return False


def write_log(): #Writes the log about the activity
    currentday = datetime.datetime.today().weekday()
    daysoftheweek = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    with open("weekly.log","r"):
        if checkday() == True: #If current day is already in the log file it only appends the activity and time to the log file
            with open("weekly.log", "a") as editlog:
                editlog.write("Activity: %s  Time Spent: %s%s \n" % (activityname, allottedtime,timetype))
        else:
            with open("weekly.log", "a") as editlog:
                editlog.write("%s \n" % daysoftheweek[currentday])
                editlog.write("Activity: %s  Time Spent: %s%s \n" % (activityname, allottedtime,timetype))

i = 0
weekpath = pathlib.Path("weekly.log")
currentweek = str(datetime.datetime.today().isocalendar()[1])
weekpath = pathlib.Path("weekly.log")
convertedtime = 0
activityname = input("What is the name of the activity you're planning on doing?")  #Get User Iputs#
allottedtime = input("How much time do you plan on giving it?")                     ################
timetype = input("Second(S),Minute(M),Hour(H)?")                                    ################
alarm = input("Do you wish to also set an alarm, when the times up? (y/n)")         ################
if timetype == "h" or timetype == "H":          # Convert the time according to "timetype"
    convertedtime = int(allottedtime) * 3600
if timetype == "m" or timetype == "M":
    convertedtime = int(allottedtime) * 60
if timetype == "s" or timetype == "S":
    convertedtime = int(allottedtime)
for i in tqdm(range(int(convertedtime))): #Displays progressbar
    time.sleep(1)
if alarm == "Y" or alarm == "y":  #Alarm
    subprocess.Popen(['notify-send',"Times Up!"])
    playsound("alarm.mp3")

if not weekpath.exists():
    open("weekly.log", "w+")
    with open("weekly.log") as logfile:
        firstline = logfile.readline().strip()

write_log()


