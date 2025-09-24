import csv
from datetime import datetime
import time
import sys
import os
import config
import statistics

libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'TSL2591/lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_TSL2591 import TSL2591

# read values every 5 seconds for 1 minute, then average
def fnc_collect_avg_values(duration_seconds=5, interval_seconds=2):
    lux_values = []
    infrared_values = []
    visible_values = []
    full_spectrum_values = []

    sensor = TSL2591.TSL2591() # init sensor
    
    try:
        for _ in range(12):
            lux_values.push(sensor.Lux) # all we're using is lux for now but store everything else just in case

            sensor.TSL2591_SET_LuxInterrupt(50, 200)
            infrared_values.push(sensor.Read_Infrared)
            visible_values.push(sensor.Read_Visible)
            full_spectrum_values.push(sensor.Read_FullSpectrum)

            time.sleep(5)  # Run every 5 seconds

        sensor.Disable() # disable sensor

        return statistics.mean(lux_values)
    
    except:
        sensor.Disable()
        return None


# Example usage:
if __name__ == "__main__":
    try:
        while True:
            fnc_collect_avg_values(60, 10)   # Collect values for x seconds with y seconds interval
            print("Waiting 5 minutes before next collection...")
            time.sleep(300)  # Sleep for 5 minutes (300 seconds)
    except KeyboardInterrupt:
        exit()

