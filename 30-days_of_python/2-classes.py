#!/usr/bin/python3
'''
We need a class able to count seconds. Easy? Not as easy as you may think, 
as we're going to have some specific requirements.

Read them carefully as the class you're about write will be used to launch rockets 
carrying international missions to Mars. It's a great responsibility. We're counting on you!

Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from the range
 [0..23] – we will be using military time), minutes (from the range [0..59]) and seconds (from the range [0..59]).

Zero is the default value for all of the above parameters. There is no need to perform any validation checks.

The class itself should provide the following facilities:

objects of the class should be "printable", i.e. they should be able to implicitly convert 
themselves into strings of the following form: "hh:mm:ss", with leading zeros added when any 
of the values is less than 10;
the class should be equipped with parameterless methods called next_second() and previous_second(),
 incrementing the time stored inside the objects by +1/-1 second respectively.
Use the following hints:

consider writing a separate function (not method!) to format the time string
'''
def time_format(value):
    if value < 10:
        value = '0'+ str(value)
    return value
class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
    def __str__(self):
        return f'{time_format(self.hours)}:{time_format(self.minutes)}:{time_format(self.seconds)}'

    def next_second(self):
        seconds=self.seconds+1
        hours=self.hours
        minutes=self.minutes
        if seconds  > 59:
            seconds = 0
            minutes+=1
            if minutes > 59:
                minutes = 0
                hours+=1
                if hours >= 24:
                    hours=0
        return Timer(hours, minutes, seconds)
    def prev_second(self):
        seconds = self.seconds - 1
        minutes = self.minutes
        hours = self.hours
        if seconds < 0:
            seconds = 59
            minutes -= 1
            if minutes < 0:
                minutes = 59
                hours -= 1
                if hours < 0:
                    hours = 23
        return Timer(hours, minutes, seconds)
hour= int(input("enter launch hour 0-24: "))
mins=int(input("enter launch minutes 0-59: "))
secs = int(input("enter launch seconds 0-59: "))
timer = Timer(hour, mins, secs)
print('Time:',timer)
timer = timer.next_second()
print('Next second:',timer)
timer = timer.prev_second()
print('Previous second:',timer)
