import time
from playsound import playsound
import os

def pomodoro_timer(pomodoros, work_duration, break_duration):
    for i in range(pomodoros):
        # Work session
        print(f"Pomodoro {i+1}: Work for {work_duration} minutes")
        playsound('relax_1.mp3')  # Play the work sound
        time.sleep(work_duration * 60)  # Convert minutes to seconds

        # Break session
        print(f"Pomodoro {i+1}: Take a break for {break_duration} minutes")
        playsound('relax_1.mp3')  # Play the break sound
        time.sleep(break_duration * 60)  # Convert minutes to seconds

    print("Congratulations! You completed all the pomodoros.")

# Rest of the code...
def clear_screen():
    # Clear the console screen
    os.system("cls" if os.name == "nt" else "clear")

def main():
    clear_screen()
    print("Pomodoro Technique Timer")
    pomodoros = int(input("Enter the number of pomodoros: "))
    work_duration = int(input("Enter the work duration (in minutes): "))
    break_duration = int(input("Enter the break duration (in minutes): "))

    pomodoro_timer(pomodoros, work_duration, break_duration)

if __name__ == "__main__":
    main()
