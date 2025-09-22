import csv
from datetime import datetime
import time
import sys
import os
import config

libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'TSL2591/lib')
#print (libdir)
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_TSL2591 import TSL2591


def fnc_collect_avg_values(duration_seconds=5, interval_seconds=2):
    lux_values = []
    infrared_values = []
    visible_values = []
    full_spectrum_values = []

    start_time = time.time()

    sensor = TSL2591.TSL2591()



    sensor.Disable()


    return avg_visible


# Example usage:
if __name__ == "__main__":
    try:
        while True:
            fnc_collect_avg_values(60, 10)   # Collect values for x seconds with y seconds interval
            print("Waiting 5 minutes before next collection...")
            time.sleep(300)  # Sleep for 5 minutes (300 seconds)
    except KeyboardInterrupt:    
        exit()

