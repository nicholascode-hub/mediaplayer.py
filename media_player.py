import tkinter as tk
import pygame
import os

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Media Player")

        # Initialize pygame mixer
        pygame.mixer.init()

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Create Play Button
        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)

        # Create Pause Button
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=10)

        # Create Stop Button
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)

    def play_music(self):
        pygame.mixer.music.load("path_to_your_music_file.mp3")  # Replace with your music file path
        pygame.mixer.music.play(loops=0)

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
