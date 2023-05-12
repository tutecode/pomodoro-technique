#import tkinter as tk
#import random
#
#def create_motivational_window(phrase_list):
#    # Select a random phrase from the list
#    phrase = random.choice(phrase_list)
#
#    # Create the main window
#    window = tk.Tk()
#    window.title("Motivational Phrases")
#    window.geometry("500x300")  # Set the window size as desired
#
#    # Create a label to display the phrase
#    label = tk.Label(window, text=phrase, font=("Arial", 24), wraplength=400)
#    label.pack(pady=50)  # Adjust the padding as needed
#
#    # Start the main event loop
#    window.mainloop()
#
## Example usage with a list of phrases
#motivational_phrases = [
#    "Stay focused and never give up!",
#    "Believe in yourself and your abilities!",
#    "Embrace challenges and grow stronger!",
#    "Success is a journey, not a destination!"
#]
#
#create_motivational_window(motivational_phrases)



import time
import pygame
import threading
import os
from PIL import Image, ImageTk
import tkinter as tk
import random


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


def pomodoro_timer(pomodoros, work_duration, break_duration, phrase_list):
    for i in range(pomodoros):
        # Work session
        print(f"Pomodoro {i+1}: Work for {work_duration} minutes")
        end_time = time.time() + (work_duration * 60)  # Calculate the end time

        while time.time() < end_time:
            # Wait for a random interval between (x, y) seconds before showing the next image
            wait_time = random.randint(240, 360) # 240, 360 sec
            time.sleep(wait_time)

            # Randomly show an image from the image list
            phrase = random.choice(phrase_list)
            threading.Thread(target=create_motivational_window, args=(phrase,)).start()


        # Break session
        print(f"Pomodoro {i+1}: Take a break for {break_duration} minutes")
        play_sound('relax_1.mp3', break_duration)
        time.sleep(break_duration * 60)  # Convert minutes to seconds

    print("Congratulations! You completed all the pomodoros.")


def clear_screen():
    # Clear the console screen
    os.system("cls" if os.name == "nt" else "clear")


def main():
    clear_screen()
    print("Pomodoro Technique Timer")
    pomodoros = int(input("Enter the number of pomodoros: "))
    work_duration = int(input("Enter the work duration (in minutes): "))
    break_duration = int(input("Enter the break duration (in minutes): "))

    # Example usage with a list of phrases
    phrase_list = [
        "Unleash the power of data and let it guide you to new frontiers.",
        "Embrace the challenges of machine learning and let them fuel your growth.",
        "Innovate fearlessly with algorithms as your brush and data as your canvas.",
        "Unlock the secrets hidden in the data, and witness the magic of machine learning unfold.",
        "Train your models with dedication, and watch them evolve into intelligence.",
        "Let your algorithms dance with the data, creating symphonies of insights.",
        "Harness the potential of machine learning to reshape the world and leave a lasting impact.",
        "Embrace the unknown, for it holds the keys to groundbreaking discoveries.",
        "Machine learning is the bridge between imagination and reality. Build it with passion.",
        "Forge ahead, one line of code at a time, and unlock the limitless possibilities of AI."
    ]

    #phrase_list = [
    #    "Start with a solid understanding of the fundamentals",
    #    "Data quality matters",
    #    "Feature selection and engineering",
    #    "Choose the right algorithm",
    #    "Evaluate and validate your models",
    #    "Regularization and hyperparameter tuning",
    #    "Ensembles and model stacking",
    #    "Continuously learn and update your models",
    #    "Understand the limitations and ethical considerations",
    #    "Stay curious and keep exploring"
    #]

    pomodoro_timer(pomodoros, work_duration, break_duration, phrase_list)


if __name__ == "__main__":
    main()
