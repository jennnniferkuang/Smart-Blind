from config import high_visible_light, low_visible_light, debug, collect_duration_seconds, collect_interval_seconds
from Read_light_sensor import fnc_collect_avg_values

# returns values open or close or do_nothing or unknown
def fnc_open_or_close(blind_status):
    # get visible_light intensity value
    print("Current blind status:", blind_status)
    if (debug):
        visible_light_intensity = fnc_collect_avg_values(30, 5) # average over 30 secs, every 5 seconds
    else:
        visible_light_intensity = fnc_collect_avg_values(collect_duration_seconds, collect_interval_seconds)
    print("visible_light Intensity average:", visible_light_intensity)
    if visible_light_intensity == -1:
        print("Error reading visible light intensity, exiting...")
        return "unknown"

    # decide whether to open or close the blinds    

    if (visible_light_intensity >= high_visible_light) & (blind_status == "opened"):
        return "close"
    
    elif (visible_light_intensity <= low_visible_light) & (blind_status == "closed"):
        return "open"
    
    else:
        return "do_nothing"
