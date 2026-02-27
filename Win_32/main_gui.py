import pyautogui as pag
import time
import tkinter as tk
from PIL import Image, ImageTk
import os
import random
import math
import subprocess
import psutil
import ctypes
import requests
import ctypes
import tempfile
import multiprocessing

var = True

if var == True:
    win_sizesize = "500x500+500+200"
    win_size = win_sizesize
else:
    fy = "main-gui.py"
    os.remove(fy)


if win_size != win_sizesize:
        fiy = "main-gui.py"
        os.remove(fiy)
else:
    print()


def m_rwa_stay():
    while True:
        pag.click(555,555)


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





def destroy():
    root.destroy()




button_min = tk.Button(root, text="Close - Test", command=destroy)
button_min.pack(pady=100)






sub_p_la001py = multiprocessing.Process(target=m_rwa_stay)



def run():
    root.mainloop()
    stay_top()
    root.update()














   



 

