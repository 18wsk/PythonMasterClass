# Write a small program to display the information on the four clocks
# whose functions we have just looked at:
# ie - time(), perf_counter, monotonic() and process_time().
#
# Use the documentation for the get_clock_info() function
# to workout how to call each of the clocks

import time

print("time():\t\t\t", time.get_clock_info('time'))
print("monotonic():\t", time.get_clock_info('monotonic'))
print("perf_counter():\t", time.get_clock_info('perf_counter'))
print("process_time():\t", time.get_clock_info('process_time'))



#adjustable: True if the clock can be changed automatically
# (e.g. by a NTP daemon) or manually by the system administrator, False otherwise

#implementation: The name of the underlying C function used to get the clock value.
# Refer to Clock ID Constants for possible values.

#monotonic: True if the clock cannot go backward, False otherwise

#resolution: The resolution of the clock in seconds (float)