"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
import datetime
 
args = sys.argv
if len(args) == 1:
  #get current month/year and render calendar
  month = datetime.date.today().month
  year = datetime.date.today().year

elif len(args) == 2:
  #assume its a month and render calendar for that month of current year
  month = int(args[1])
  year = datetime.date.today().year
  
elif len(args) == 3:
  #render calendar for month and year entered
  month = int(args[1])
  year = int(args[2])

else:
  print('Too many arguments: program expects 0, 1 (int month), or 2 (int month & int year)')

cal = calendar.TextCalendar(calendar.SUNDAY)
cal.prmonth(theyear=year, themonth=month)