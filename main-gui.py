import pyautogui
import time
import tkinter as tk
from PIL import Image, ImageTk
import os

root = tk.Tk()
i = 0

os.system("cd Downloads")
img_path = "C:/Users/<USER>/Downloads/py_logo.png"
image_pil = Image.open(img_path)
image_tk = ImageTk.PhotoImage(image_pil)
image_label = tk.Label(root, image=image_tk)
image_label.image = image_tk
image_label.pack(pady=20)

def min_win():
    root.iconify()

def close_win():
    root.protocol("WM_DELETE_WINDOW", True)

root.title("Display Image - Template")
root.geometry("250x200")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", False)
root.protocol("WM_MINIMIZE_WINDOW", False)

# button_min = tk.Button(root, text="Minimize Window", command=min_win)
# button_min.pack(pady=100)





root.mainloop()


   



 
