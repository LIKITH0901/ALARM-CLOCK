import datetime
import time
import winsound

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == alarm_time:
            print("Wake up!")
            for _ in range(5):
                winsound.Beep(1000, 1000)  # frequency, duration
            break
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter alarm time (HH:MM, 24-hour format): ")
    set_alarm(alarm_time)