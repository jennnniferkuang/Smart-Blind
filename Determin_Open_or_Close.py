from config import high_visible_light, low_visible_light
from Read_light_sensor import fnc_collect_avg_values

# returns values open or close or do_nothing or unknown
def fnc_open_or_close(blind_status):
    #get visible_light intensity value
    visible_light_intensity = fnc_collect_avg_values(120,10) #average over 1 minute
    print("visible_light Intensity average:", visible_light_intensity)
    if visible_light_intensity == -1:
        print("Error reading visible light intensity, exiting...")
        return "unknown"

    #decide whether to open or close the blinds    

    if visible_light_intensity >= high_visible_light:
        return "open"
    
    elif visible_light_intensity <= low_visible_light:
        return "close"
    
    else:
        return "do_nothing"
