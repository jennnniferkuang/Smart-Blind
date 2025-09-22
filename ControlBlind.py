
#Adafruit Python DHT Sensor Library

# This script sends an HTTP request to a specified URL and prints the response. 
import requests
import urllib3
import time
import config


#function to send command to the smart blind controller
def fnc_send_command(room_id, blind_id, command):
    # Suppress only the single InsecureRequestWarning from urllib3 needed.
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    current_millis = int(time.time() * 1000)
    hash_value = str(current_millis)[-7:]
    params = {
        "command": f"{room_id}-{blind_id}-{command}!bf", #id1.id2-channel-command!motor_type
        "id": "Vce0i0JPWN-6zBaqMlbwjw", #controller device id , never change it
        "hash": hash_value #unique hash value for each request to prevent duplicate processing
    }
    try:
        response = requests.get(config.Controller_URL, params=params, verify=False, timeout=10)        
        if config.debug: 
            print("Status Code:", response.status_code)
            print("Response Body:", response.text)
        if response.status_code >= 200 and response.status_code < 300:
            return 1
        else:
            return 0
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return 0

#function to control blinds in living room and breakfast nook
def fnc_control_all_blinds(command):
    ret = 1
    #send command to control all blinds
    if fnc_send_command(config.living_room, config.living_all_blind, command)!=1:
        ret =0
        if config.debug: print("Failed to send command to living room blinds")
    time.sleep(2) #wait for 2 seconds before sending next command
    if fnc_send_command(config.breakfast_nook, config.nook_blind, command)!=1:
        ret =0
        if config.debug: print("Failed to send command to breakfast nook blind")
    return ret


#example usage, run this to test it directly: python SendHTTPReq.py
if __name__ == "__main__":
    if fnc_send_command(config.living_room, config.living_left_blind, "dn"):
        print("fnc_send_command: Command sent successfully")
    else:
        print("fnc_send_command: Failed to send command") 


