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

def fnc_collect_avg_values(duration_seconds=300, interval_seconds=10):
    lux_values = []
    infrared_values = []
    visible_values = []
    full_spectrum_values = []

    sensor = TSL2591.TSL2591() # init sensor
    
    while duration_seconds > 0:
        lux_values.append(sensor.Lux)
        sensor.TSL2591_SET_LuxInterrupt(50, 200)
        infrared_values.append(sensor.Read_Infrared)
        visible_values.append(sensor.Read_Visible) # only using visible light for now
        full_spectrum_values.append(sensor.Read_FullSpectrum)

        duration_seconds -= interval_seconds
        time.sleep(interval_seconds)

    sensor.Disable() # disable sensor

    return statistics.mean(visible_values)
    
    # except:
    #     sensor.Disable()
    #     return None


# Example usage:
if __name__ == "__main__":
    try:
        while True:
            avg_val = fnc_collect_avg_values()
            print(f"Average Lux value over collection period: {avg_val}")
            print("Waiting 20 secs before next collection...")
            time.sleep(20)  # Sleep for n seconds
    except KeyboardInterrupt:
        exit()

