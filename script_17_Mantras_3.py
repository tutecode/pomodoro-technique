import time
import pygame
import threading
import os
from PIL import Image, ImageTk
import tkinter as tk
import random
import csv
from datetime import datetime
import tkinter.font as tkfont

# from winroundedcorners import RoundedCornersWindow  # for Windows
# from pyglet import window  # for Mac
import random


def play_sound(file_path, duration):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)

    # Schedule a stop event after the specified duration
    threading.Timer(duration * 60, pygame.mixer.music.stop).start()


def insert_csv(description, work_duration, break_duration):
    # Check if the CSV file exists
    file_exists = os.path.isfile("pomodoro_data.csv")

    # Write the data to the CSV file
    with open("pomodoro_data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)

        # Write header row if the file is newly created
        if not file_exists:
            writer.writerow(["Date", "Description", "Work", "Break"])

        # Get the current date and time
        current_datetime = datetime.now()

        writer.writerow([current_datetime, description, work_duration, break_duration])


def create_motivational_window(phrase):
    # Select a random phrase from the list
    # phrase = random.choice(phrase)

    # Create the main window
    window = tk.Tk()
    window.title("Remember")

    # Determine the width of the phrase
    # phrase_width = len(phrase) * 5  # Adjust the multiplier as needed for desired window width
    # phrase_height = len(phrase) // 10  # Adjust the divisor as needed for desired window height

    # phrase_width = len(phrase)  # Adjust the multiplier as needed for desired window width
    # phrase_height = len(phrase)  # Adjust the divisor as needed for desired window height

    phrase_width = 500
    phrase_height = 200

    # Set the window size based on the phrase width
    window.geometry(f"{phrase_width}x{phrase_height*20}")
    # window.geometry(f"{phrase_width}x{phrase_height}")
    # window.geometry("500x200")  # Set the window size as desired

    # Create a label to display the phrase
    # label = tk.Label(window, text=phrase, font=("Arial", 16))
    label = tk.Label(window, text=phrase, font=("Arial", 16), wraplength=phrase_width)

    label.pack(pady=10000)  # Adjust the padding as needed

    # Calculate random coordinates for the image position
    # window.update()  # Ensure window dimensions are updated
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = random.randint(0, phrase_width - window_width)
    y = random.randint(0, phrase_height - window_height)

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Make the window stay on top
    window.attributes("-topmost", True)

    # Start the main event loop
    window.after(10000, window.destroy)  # Close the window after 3 seconds
    window.mainloop()


def create_motivational_window_2(phrase):
    # Create the main window
    window = tk.Tk()
    window.title("Remember")

    # Determine the width and height of the phrase
    phrase_width = (
        len(phrase) * 15
    )  # Adjust the multiplier as needed for desired window width
    # phrase_height = len(phrase) * 8
    phrase_height = 105

    # Set the window size based on the phrase dimensions
    window.geometry(f"{phrase_width}x{phrase_height}")

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate random coordinates for the window position
    x = random.randint(0, screen_width - phrase_width)
    y = random.randint(0, screen_height - phrase_height)

    # Position the window at the random coordinates
    window.geometry(f"+{x}+{y}")

    # Create a label to display the phrase
    label = tk.Label(window, text=phrase, font=("Arial", 24), wraplength=phrase_width)
    label.pack(pady=20)  # Adjust the padding as needed

    # Make the window stay on top
    window.attributes("-topmost", True)

    # Start the main event loop
    window.after(3000, window.destroy)  # Close the window after 3 seconds
    window.mainloop()


def quitter():
    window = tk.Tk()
    window.quit()


def on_exit_enter(event):
    # Apply a transparent highlight effect
    event.widget.image = event.widget.image_tk  # Restore the original image
    event.widget.image.putalpha(128)  # Set the alpha channel to 128 (semi-transparent)
    event.widget.config(image=event.widget.image)  # Update the image on the label

def on_exit_leave(event):
    # Restore the original image
    event.widget.config(image=event.widget.image_tk)

def create_motivational_window_3(phrase):
    # Create the main window
    window = tk.Tk()
    window.title("Remember")
    
    # Remove title bar
    window.overrideredirect(True)

    # Configure header colors and font
    header_bg = "#003049"  # Background color
    header_fg = "#FFFFFF"  # Text color

    # Create a header frame
    header_frame = tk.Frame(window, bg=header_bg)
    header_frame.pack(fill="x")

    # Exit button icon
    exit_icon = Image.open('cross_red.png').convert("RGBA")

    # Apply initial transparency to the image
    exit_icon.putalpha(128)  # Set the alpha channel to 128 (semi-transparent)

    # Convert the image to Tkinter PhotoImage
    exit_image_tk = ImageTk.PhotoImage(exit_icon)

    # Create the exit label with the initial transparent image
    exit_label = tk.Label(header_frame, image=exit_image_tk, border=0, bg=header_bg)
    exit_label.image_tk = exit_image_tk  # Store a reference to the PhotoImage
    exit_label.pack(side='right', pady=5, padx=10)  # Add a right margin using padx

    # Bind the quit function to the exit label
    exit_label.bind('<Button-1>', lambda e: window.quit())

    # Bind hover events to the exit label
    exit_label.bind('<Enter>', on_exit_enter)
    exit_label.bind('<Leave>', on_exit_leave)

    # Determine the width and height of the phrase
    phrase_width = len(phrase) * 15  # Adjust the multiplier as needed for desired window width
    phrase_height = 150  # Adjust the height as desired

    # Set the window size based on the phrase dimensions
    window.geometry(f"{phrase_width}x{phrase_height}")

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate random coordinates for the window position
    x = random.randint(0, screen_width - phrase_width)
    y = random.randint(0, screen_height - phrase_height)

    # Position the window at the random coordinates
    window.geometry(f"+{x}+{y}")

    # Create a label to display the phrase
    label = tk.Label(window, text=phrase, font=("Perpetua", 24), wraplength=phrase_width)
    label.pack(pady=20)  # Adjust the padding as needed

    # Make the window stay on top
    window.attributes("-topmost", True)

    # Start the main event loop
    window.after(5000, window.destroy)  # Close the window after 5 seconds
    window.mainloop()





def show_final_image(image_path):
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


def create_motivational_window_4(phrase):
    # Create the main window
    window = RoundedCornersWindow()  # for Windows
    # window = window.Window()  # for Mac
    window.title("Remember")

    # Remove title bar
    window.overrideredirect(True)

    # Configure header colors and font
    header_bg = "#003049"  # Background color
    header_fg = "#FFFFFF"  # Text color
    header_font = ("Arial", 13, "bold")

    # Create a header frame
    header_frame = tk.Frame(window, bg=header_bg)
    header_frame.pack(fill="x")

    # Create a label for the header text
    header_label = tk.Label(
        header_frame, text="Remember", font=header_font, fg=header_fg, bg=header_bg
    )
    header_label.pack(side="left", pady=5)

    # Create a close button on titlebar
    close_label = tk.Label(
        header_frame, text="  X  ", bg=header_bg, fg="white", relief="raised", bd=1
    )
    close_label.pack(side="right", pady=5, ipadx=1)
    close_label.bind("<Button-1>", quitter)

    # Determine the width and height of the phrase
    phrase_width = (
        len(phrase) * 15
    )  # Adjust the multiplier as needed for desired window width
    phrase_height = 150  # Adjust the height as desired

    # Set the window size based on the phrase dimensions
    window.geometry(f"{phrase_width}x{phrase_height}")

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate random coordinates for the window position
    x = random.randint(0, screen_width - phrase_width)
    y = random.randint(0, screen_height - phrase_height)

    # Position the window at the random coordinates
    window.geometry(f"+{x}+{y}")

    # Create a label to display the phrase
    label = tk.Label(
        window, text=phrase, font=("Perpetua", 24), wraplength=phrase_width
    )
    label.pack(pady=20)  # Adjust the padding as needed

    # Make the window stay on top
    window.attributes("-topmost", True)

    # Start the main event loop
    window.after(5000, window.destroy)  # Close the window after 3 seconds
    window.mainloop()


def show_finish_window(
    pomodoros, description, work_duration, break_duration, phrase_list
):
    window = tk.Tk()
    window.title("Pomodoro Finished")

    label = tk.Label(window, text="Did you finish your job? (yes/no)")
    label.pack(pady=50)

    def start_pomodoro():
        window.destroy()
        show_final_image("capo.jpg")

    def quit_program():
        window.destroy()
        insert_csv(description, work_duration, break_duration)
        pomodoro_timer(
            pomodoros, description, work_duration, break_duration, phrase_list
        )

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
        play_sound("relax_1.mp3", break_duration)
        time.sleep(break_duration * 60)

    show_finish_window(
        pomodoros, description, work_duration, break_duration, phrase_list
    )


def clear_screen():
    # Clear the console screen
    os.system("cls" if os.name == "nt" else "clear")


def main():
    # clear_screen()
    # print("Pomodoro Technique Timer")
    # pomodoros = int(input("Enter the number of pomodoros: "))
    # work_duration = int(input("Enter the work duration (in minutes): "))
    # break_duration = int(input("Enter the break duration (in minutes): "))
    # description = input("Enter a description: ")
    # insert_csv(description, work_duration, break_duration)

    # Example usage with a list of phrases
    phrase_list = [
        "¡Valórate!",
        "Haz ejercicio cabrón!",
        "Touch some grass",
        "Llama a tus seres queridos",
        "¡Valórate!",
        "¡Valórate!",
    ]
    phrase = random.choice(phrase_list)
    create_motivational_window_3(phrase)

    # pomodoro_timer(pomodoros, description, work_duration, break_duration, phrase_list)


if __name__ == "__main__":
    main()
