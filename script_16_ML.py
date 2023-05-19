import time
import pygame
import threading
import os
from PIL import Image, ImageTk
import tkinter as tk
import random
import csv
from datetime import datetime


def play_sound(file_path, duration):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)

    # Schedule a stop event after the specified duration
    threading.Timer(duration * 60, pygame.mixer.music.stop).start()


def create_motivational_window(phrase):
    # Select a random phrase from the list
    #phrase = random.choice(phrase)

    # Create the main window
    window = tk.Tk()
    window.title("Motivational Phrases")
    #window.geometry("500x200")  # Set the window size as desired

    # Determine the width of the phrase
    phrase_width = len(phrase) * 5  # Adjust the multiplier as needed for desired window width
    phrase_height = len(phrase) // 10  # Adjust the divisor as needed for desired window height

    
    # Set the window size based on the phrase width
    window.geometry(f"{phrase_width}x{phrase_height*20}")

    # Create a label to display the phrase
    label = tk.Label(window, text=phrase, font=("Arial", 16), wraplength=phrase_width)
    label.pack(pady=50)  # Adjust the padding as needed

    window.attributes("-topmost", True)  # Make the window stay on top

    # Start the main event loop
    window.after(5000, window.destroy)  # Close the window after 3 seconds
    window.mainloop()


def show_finish_window(pomodoros, description, work_duration, break_duration, phrase_list):
    window = tk.Tk()
    window.title("Pomodoro Finished")

    label = tk.Label(window, text="Did you finish your job? (yes/no)")
    label.pack(pady=50)

    def start_pomodoro():
        window.destroy()
        main()

    def quit_program():
        window.destroy()
        pomodoro_timer(pomodoros, description, work_duration, break_duration, phrase_list)


    yes_button = tk.Button(window, text="Yes", command=start_pomodoro)
    yes_button.pack(side="left", padx=10)

    no_button = tk.Button(window, text="No", command=quit_program)
    no_button.pack(side="right", padx=10)

    window.mainloop()


def pomodoro_timer(pomodoros, description, work_duration, break_duration, phrase_list):
    for i in range(pomodoros):
        print(f"Pomodoro {i+1}: Work for {work_duration} minutes")
        end_time = time.time() + (work_duration * 60)

        while time.time() < end_time:
            wait_time = random.randint(240, 360)
            time.sleep(wait_time)

            phrase = random.choice(phrase_list)
            threading.Thread(target=create_motivational_window, args=(phrase,)).start()

        print(f"Pomodoro {i+1}: Take a break for {break_duration} minutes")
        play_sound('relax_1.mp3', break_duration)
        time.sleep(break_duration * 60)

    show_finish_window(pomodoros, description, work_duration, break_duration, phrase_list)



def clear_screen():
    # Clear the console screen
    os.system("cls" if os.name == "nt" else "clear")


#def start_pomodoro():
#    pomodoros = int(pomodoros_entry.get())
#    work_duration = int(work_duration_entry.get())
#    break_duration = int(break_duration_entry.get())
#    #description = description_entry.get()
#
#    # Save the configuration values to a file
#    with open("config.txt", mode="w") as file:
#        file.write(f"{pomodoros}\n")
#        file.write(f"{work_duration}\n")
#        file.write(f"{break_duration}\n")
#
#    # Close the window and start the pomodoro timer
#    window.destroy()
#    pomodoro_timer(pomodoros, work_duration, break_duration)


def start_pomodoro():
    pomodoros = int(pomodoros_entry.get())
    work_duration = int(work_duration_entry.get())
    break_duration = int(break_duration_entry.get())
    description = description_entry.get()

    # Save the configuration values to a file
    with open("config.txt", mode="w") as file:
        file.write(f"{pomodoros}\n")
        file.write(f"{work_duration}\n")
        file.write(f"{break_duration}\n")
        file.write(f"{description}\n")

    # Close the window and start the pomodoro timer
    window.destroy()
    pomodoro_timer(pomodoros, description, work_duration, break_duration, phrase_list)

def main():
    global window, pomodoros_entry, work_duration_entry, break_duration_entry, description_entry

    window = tk.Tk()
    window.title("Pomodoro Technique Timer")

    pomodoros_label = tk.Label(window, text="Number of Pomodoros:")
    pomodoros_label.pack()
    pomodoros_entry = tk.Entry(window)
    pomodoros_entry.pack()

    work_duration_label = tk.Label(window, text="Work Duration (minutes):")
    work_duration_label.pack()
    work_duration_entry = tk.Entry(window)
    work_duration_entry.pack()

    break_duration_label = tk.Label(window, text="Break Duration (minutes):")
    break_duration_label.pack()
    break_duration_entry = tk.Entry(window)
    break_duration_entry.pack()

    description_label = tk.Label(window, text="Description:")
    description_label.pack()
    description_entry = tk.Entry(window)
    description_entry.pack()

    start_button = tk.Button(window, text="Start", command=start_pomodoro)
    start_button.pack()

    window.mainloop()


if __name__ == "__main__":
    clear_screen()
    print("Pomodoro Technique Timer")

    # Check if there is a saved configuration
    config_file_exists = os.path.isfile("config.txt")

    if config_file_exists:
        # Read the values from the configuration file
        with open("config.txt", mode="r") as file:
            config_data = file.readlines()
            pomodoros = int(config_data[0])
            work_duration = int(config_data[1])
            break_duration = int(config_data[2])
            description = config_data[3].strip()
    else:
        # Start the GUI for inputting values if no configuration file exists
        main()

    # Example usage with a list of phrases
    phrase_list = [
        "Unleash",
        "Embrace",
        "Innovate",
    ]

    pomodoro_timer(pomodoros, description, work_duration, break_duration, phrase_list)

