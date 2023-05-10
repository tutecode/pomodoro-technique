import time
import pygame
import threading
import os
from PIL import Image, ImageTk
import tkinter as tk
import random
from tkinter import PhotoImage


def play_sound(file_path, duration):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)

    # Schedule a stop event after the specified duration
    threading.Timer(duration * 60, pygame.mixer.music.stop).start()


def show_image(image_path):
    # Create the main window
    window = tk.Tk()
    window.title("Image Viewer")
    window.attributes("-topmost", True)  # Make the window stay on top

    # Load the image
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    # Get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate random position
    image_width = photo.width()
    image_height = photo.height()
    x = random.randint(0, screen_width - image_width)
    y = random.randint(0, screen_height - image_height)

    # Create a canvas to display the image
    canvas = tk.Canvas(window, width=image_width, height=image_height)
    canvas.pack()
    canvas.create_image(x, y, anchor=tk.NW, image=photo)

    # Start the main event loop
    window.after(10000, window.destroy)  # Close the window after 5 seconds
    window.mainloop()


def pomodoro_timer(pomodoros, work_duration, break_duration):
    for i in range(pomodoros):
        # Work session
        print(f"Pomodoro {i+1}: Work for {work_duration} minutes")
        # play_sound('work_sound.wav', work_duration)
        time.sleep(work_duration * 60)  # Convert minutes to seconds

        # Break session with image display
        print(f"Pomodoro {i+1}: Take a break for {break_duration} minutes")
        threading.Thread(target=show_image, args=('frase_1.png',)).start()  # Replace 'image.jpg' with your image file path
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

    pomodoro_timer(pomodoros, work_duration, break_duration)


if __name__ == "__main__":
    main()
