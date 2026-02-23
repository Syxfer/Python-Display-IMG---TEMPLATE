import pyautogui as pag
import time
import tkinter as tk
from PIL import Image, ImageTk
import os
import sys
import random
import math
import subprocess
import psutil

import ctypes
import os

import requests
import ctypes
import os
import tempfile

def set_wallpaper_from_url(image_url):

    response = requests.get(image_url)
    if response.status_code != 200:
        print(f"Failed to download image from {image_url}")
        return


    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, "temp_wallpaper.bmp")

    with open(temp_path, 'wb') as f:
        f.write(response.content)

    ctypes.windll.user32.SystemParametersInfoW(20, 0, temp_path, 3)

    print(f"Wallpaper set successfully from {image_url}")

github_image_url = "https://raw.githubusercontent.com/Syxfer/HOST-IMG/blob/main/test.png" 

set_wallpaper_from_url(github_image_url)

while True:
    pag.click(750,400)
    break
    





root = tk.Tk()
i = 0
root.overrideredirect(True)

win_size = "500x500+500+200"
def stay_top():
    top_window = tk.Toplevel(root)
    top_window.attributes('-topmost', True)


os.system("cd Downloads")
img_path = "source-imgs/py_logo.png"
image_pil = Image.open(img_path)
image_tk = ImageTk.PhotoImage(image_pil)
image_label = tk.Label(root, image=image_tk)
image_label.image = image_tk
image_label.pack(pady=20)

def min_win():
    root.iconify()
    

def close_win():
    root.protocol("WM_DELETE_WINDOW", True)

root.title("")
root.geometry(win_size)
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", False)
in_x = tk.Entry()
in_x.pack()
x_in = in_x.get()

if x_in == "hi":
    root.destroy()
else:
    print()








button_min = tk.Button(root, text="Minimize Window", command=min_win)
button_min.pack(pady=100)









def run():
    root.mainloop()
    stay_top()
    root.update()

run()


   



 
