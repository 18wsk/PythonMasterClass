# import time
# print(time.gmtime(0))
#
# print(time.localtime())
#
# print(time.time())  # number of seconds since epoch

# gmtime and local time -> convert number of seconds into a named struct_time tuple
########################################################################
# import time

# print(time.gmtime(0))
# time_here = time.localtime()
#
# print(time_here)
# print("Year: ", time_here[0], time_here.tm_year)
# print("Month: ", time_here[1], time_here.tm_mon)
# print("Day: ", time_here[2], time_here.tm_mday)
########################################################################
import time
from time import process_time as my_timer
import random
# time -> measures real time

# perf_counter -> returns the float value of time in sec -> time elapsed during sleep and is system-wide

# monotonic -> Monotonic clocks are unidirectional. They can only go forward.
# This means that they are only useful in giving you relative times – the times between two events.

# process_time -> returns “the sum of the system and user CPU time of the current process.”
# It only counts time spent on the process in question

input("Please Enter to Start: ")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()     # stores current time at start time
input("Press Enter to stop: ")

end_time = my_timer()       # stores end time in that variable

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))
# %x = local date .... %X = local time
# time.strftime -> converts time to more readable string

print("Your reaction time was {} seconds".format((end_time - start_time)))
########################################################################
