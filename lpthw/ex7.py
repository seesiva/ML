"""
Python program to display todays date and time
"""
import datetime

now = datetime.datetime.now()
print now
print (now.strftime("%Y-%m-%d %H:%M:%S")) 
""" 
Read the datetime tuple
"""
dt = datetime.datetime.now()
tt = dt.timetuple()
for it in tt:   
    print it
