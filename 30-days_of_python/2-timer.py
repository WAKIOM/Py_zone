#!/usr/bin/python3
#wrote a simple program that takes input from user about starting time of an
#event in hr:min format  and its duration then it calulates the expected ending time
#For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16
#take input from user
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
duration = int(input("Event duration (minutes): "))

#convert start time into minutes
start_time_in_mins = hour * 60 + mins
#get ending time 
end_time_in_mins = start_time_in_mins + duration
#convert end time into hours and minutes
hours = (end_time_in_mins // 60) % 24
minutes= end_time_in_mins % 60
#Format the minutes with a leading zero if less than 10
minutes = f"{minutes:02d}"
if 0 <= hours < 12:
    print( "Event ends at {}:{} AM".format(hours, minutes))
else:
    print( "Event ends at {}:{} PM".format(hours, minutes))


