from datetime import datetime
from playsound import playsound

setTime = input("Enter the time of alarm to be set:HH:MM:SS\n ")
alarm_hour=setTime[0:2]
alarm_minute=setTime[3:5]
alarm_seconds=setTime[6:8]





while True:
    # Set Alarm
    set_alarm = f"{alarm_hour}:{alarm_minute}:{alarm_seconds}"
    
 
    # Get current time
    current_time = datetime.now().strftime("%H:%M:%S")
 
    # Check whether set alarm is equal to current time or not
    if current_time == set_alarm:
        print("Time to Wake up")
        print("Wake Up!")
        playsound("alarm.wav")
        break
        
    