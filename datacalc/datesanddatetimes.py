# import time
#
# print("The epoch on this system starts at: " + time.strftime("%c", time.gmtime(0)))
# # gmtime()->Convert a time expressed in seconds since the epoch to a struct_time in UTC in which the dst flag is always zero
#
# print("The current timezone is {0} with and offset of {1}".format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print("\tDaylight Saving Time is in effect for this location")
#     print("\tThe DST timezone is: " + time.tzname[1])
#
# print("Local time is " +time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print("UTC time is " +time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())