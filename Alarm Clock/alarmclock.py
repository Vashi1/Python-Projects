from playsound import playsound
import time

#Important Escape Sequences for Clearing the Terminal
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}min:{seconds_left:02d}sec")
    playsound("Alarm.mp3")

min = int(input("The no. of minutes you want to wait: "))
sec = int(input("The no. of seconds you want to wait: "))
total_seconds = (min * 60) + sec
alarm(total_seconds)