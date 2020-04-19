# Using Time and Calendar module, Print current date and time. Print current month calendar.
#
import calendar

yy = 2019
mm = 10
dd = 21
# print(dir(calendar))
print(calendar.month(yy,mm,dd))

import time

t =time.localtime()
current_time_Date = time.strftime("%d/%m/%Y %H:%M:%S", t)
print(current_time_Date)

# import time,datetime
#
# today = datetime.date.today()
# print(today)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S", t)
# print(current_time)
#
#
# now = datetime.now()
# print(now)

# By using Datetime module

# from datetime import datetime
#
# # datetime object containing current date and time
# now = datetime.now()
#
# print("now =", now)
# # dd/mm/YY H:M:S
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", dt_string)
#
