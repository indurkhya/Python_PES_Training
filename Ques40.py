# 40	Dictionary  and Date & Time	Using time module perform following operations.
# a) Print current time for every 5 seconds up to 1 minute time interval.
# b) Write a program to find out how much CPU time is taken for the execution of above(32.a)  program.


import time
t =time.localtime()
print(type(t))
current_time_Date = time.strftime("%d/%m/%Y %H:%M:%S", t)
# print(current_time_Date)

dict = {"Date":time.strftime("%d/%m/%Y"),"Time":time.strftime("%H:%M:%S", t)}
print(dict)

# total_sec=60
# while total_sec >0:
#   print(time.asctime(time.localtime(time.time())))
#   time.sleep(5)
#   total_sec-=5

# By using ctime function
# print("The time is      :", time.ctime())
# later = time.time() + 5
# time.sleep(5)
# print("5 secs from now :", time.ctime(later))


start_time=time.time()
print(start_time)
List1=[1,2,3,4,5,6,7]
List2=[6,7,8,9]
List3=[4,1,2,3]
print("Three lists \n",List1,List2,List3)
#a
print("Length of the List1 is ",len(List1))
print("Length of the List2 is ",len(List2))
print("Length of the List3 is ",len(List3))
end_time=time.time()
print(end_time)
cpu_time=end_time-start_time
print("Approximate cpu time taken to execute above task is ",cpu_time," seconds")




