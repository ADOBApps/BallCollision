"""
# Author: Acxel Orozco
# Date: 14/09/2022
"""
import tkinter as tk
from myviews.ui.windows import Windows


def launcher():
    '''
    Start Graphic User Interface (Windows module)
    '''
    # Tk man
    root = tk.Tk()
    # Screen dimension
    screen_width = round(root.winfo_screenwidth() * 0.80)
    screen_height = round(root.winfo_screenheight() * 0.80)
    root.geometry(f"{screen_width}x{screen_height}")
    root.title("Ball collision")
    window = Windows(root)
    window.Ballconfig()
    root.mainloop()


if __name__ == "__main__":
    launcher()
