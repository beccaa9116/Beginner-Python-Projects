import time
from playsound import playsound

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
 time_elapsed = 0

 print(CLEAR)

 while time_elapsed < seconds:
  time.sleep(1)
  time_elapsed += 1

  time_to_go = seconds - time_elapsed
  minutes_to_go = time_to_go // 60
  seconds_to_go = time_to_go % 60

  print(f"{CLEAR_AND_RETURN}Your alarm is set to go off in: {minutes_to_go:02d}:{seconds_to_go:02d}")
 playsound("alarm.mp3")

minutes = int(input("Set minutes for your timer here: "))
seconds = int(input("Add seconds if you want to: "))

alarm_time = minutes*60 + seconds
alarm(alarm_time)