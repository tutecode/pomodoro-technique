import pygame
import tkinter as tk

def initialize_pygame():
    pygame.mixer.init()

def play_sound(file_path, duration):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)

    # Schedule a stop event after the specified duration
    pygame.time.set_timer(pygame.USEREVENT + 1, int(duration * 1000))

def stop_sound():
    pygame.mixer.music.stop()

def create_mute_window(file_path, duration):
    window = tk.Tk()
    window.title("Music Player")

    def mute_music():
        stop_sound()

    mute_button = tk.Button(window, text="Mute", command=mute_music)
    mute_button.pack(pady=20)

    window.after(1000, lambda: play_sound(file_path, duration))
    window.mainloop()

# Example usage
create_mute_window("relax_1.mp3", 10)  # Replace "music.mp3" with your own audio file path and specify the duration

