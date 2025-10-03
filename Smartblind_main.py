#this script will be scheduled to run every hour using cron job in linux
#it will check the visible light intensity using a light sensor connected to Raspberry Pi
#if the intensity is above a certain threshold defined in config, it will send command to the smart blind controller to
#close the blinds, otherwise it will open the blinds(if they are closed)

import config
from ControlBlind import fnc_control_all_blinds
from Determine_Open_or_Close import fnc_open_or_close
import time
from datetime import datetime

#main function
def main():
    blind_current_status = "opened" #initial status
    num_of_operations = 0 #prevent excessive number of operations

    while True:
        #stop control after 8pm or after 4 operations
        now = datetime.now()
        if now.hour >= 20: 
            print("It's 8pm or later, exiting blind control program.")
            break
        if num_of_operations >= 4:
            print("Maximum number of operations reached for today, exiting blind control program.")
            break
        
        #decide whether to open or close the blinds based on visible light intensity
        open_or_close = fnc_open_or_close(blind_current_status)
        print("Decision to open or close the blinds:", open_or_close)

        if open_or_close == "do_nothing":
            if config.debug: print("No action needed, waiting...")
        else:
            if open_or_close == "open":
                if config.debug: print("performing action open...")
                if fnc_control_all_blinds("up") == 1:
                    blind_current_status = "opened"
                    num_of_operations += 1
                    print(f"Blinds opened due to low visible_light intensity at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                else:
                    print("Failed to open blinds")
            elif open_or_close == "close":
                if config.debug: print("performing action close...")
                if fnc_control_all_blinds("gp") == 1:
                    blind_current_status = "closed"
                    num_of_operations += 1
                    print(f"Blinds closed due to high visible_light intensity  at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                else:
                    print("Failed to close blinds")
            else:
                print("Received unknown decision, please check for issue...")

        if (config.debug):
            time.sleep(10)
        else:
            time.sleep(config.rest_duration_seconds)
    

if __name__ == "__main__":
    main() 

