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


def show_image(image_path):
    # Load the image
    image = Image.open(image_path)

    # Create the main window with the same size as the image
    window = tk.Tk()
    window.title("Image Viewer")




    ####################################
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Calculate random coordinates for the image position
    x = random.randint(0, screen_width - image.width)
    y = random.randint(0, screen_height - image.height)

    window.geometry(f"{image.width}x{image.height}+{x}+{y}")
    ######################################


    window.attributes("-topmost", True)  # Make the window stay on top

    # Convert the image to PhotoImage
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    label = tk.Label(window, image=photo)
    label.pack()

    # Start the main event loop
    window.after(6000, window.destroy)  # Close the window after 3 seconds
    window.mainloop()


def pomodoro_timer(pomodoros, work_duration, break_duration, image_list):
    for i in range(pomodoros):
        # Work session
        print(f"Pomodoro {i+1}: Work for {work_duration} minutes")
        end_time = time.time() + (work_duration * 60)  # Calculate the end time

        while time.time() < end_time:
            # Wait for a random interval between 10 to 30 seconds before showing the next image
            wait_time = random.randint(10, 30)
            # wait_time = random.randint(240, 360)
            time.sleep(wait_time)

            # Randomly show an image from the image list
            image_path = random.choice(image_list)
            threading.Thread(target=show_image, args=(image_path,)).start()


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

    image_list = [
        'C:/Users/Matías/Desktop/pomodoro-technique/frase_1.png',
        "C:/Users/Matías/Desktop/pomodoro-technique/frase_2.png",
        'C:/Users/Matías/Desktop/pomodoro-technique/Gonza-matenme.jpg'
        # Add more image paths as needed
    ]

    pomodoro_timer(pomodoros, work_duration, break_duration, image_list)


if __name__ == "__main__":
    main()
