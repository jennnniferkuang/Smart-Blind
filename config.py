
# To start new project, first create Python virtual environment using your desired python version
# create and cd to the project folder, then issue: <Python directory>\python -m venv myenv
# then active it in bash terminal: source myenv/bin/activate
# later on if you import any other 3rd party modules, it will be installed in this project folder,
# you can also export the list of modules to requirements.txt file: pip freeze > requirements.txt

#this file defines all constants used in the project

#Neo Smart Blind Controller URL
Controller_URL="http://192.168.1.67:8838/neo/v1/transmit" #controller IP address, it rarely changes unless controller or router reset

#Room and Blind IDs
#these values are defined in the controller, never change
living_room = "073.067" 
living_main_blind = "01"
living_left_blind = "02"
living_all_blind= "15"

breakfast_nook = "119.019"
nook_blind = "01"

porch = "066.198"
porch_blind = "02"

#global variables
debug = False #set to True to enable debug messages, False to surpress them
# debug = True


high_visible_light  = 140000000 #threshold value to close the blinds, adjust it as needed
low_visible_light = 45000000 #threshold value to raise the blinds, adjust it as needed

# valid blind commands are as follows
# "up” : blinds move UP
# “dn” : blinds move DOWN
# “sp” : blinds STOP moving
# “gp” : go to favourite position
# “mu” : micro-step up
# “md” : micro-step down

collect_duration_seconds = 300 # 5 minutes
collect_interval_seconds = 10  # every 10 seconds
rest_duration_seconds = 1800 # 30 minutes rest between collections