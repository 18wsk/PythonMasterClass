import tkinter as tk
import pygame

music_play_count = 1
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\Willi\Desktop\Code\Music\Travis Scott - SICKO MODE (Audio).mp3")


def play_music():
    global music_play_count
    music_play_count -= 1
    if music_play_count == 0:
        pygame.mixer.music.play()
        music_play_count -= 1
    else:
        pygame.mixer.music.stop()
        music_play_count += 1


print(music_play_count)
mainWindow = tk.Tk()
keekeeButton = tk.Button(mainWindow, text="KeeKeeButton", command=play_music)
keekeeButton.grid(row=0, column=0, sticky="ew", columnspan=8)
mainWindow.update()
mainWindow.mainloop()

