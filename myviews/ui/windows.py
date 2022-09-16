"""
# Author: Acxel Orozco
# Date: 14/09/2022
"""

import tkinter as tk
from tkinter import Button
from tkinter import messagebox as mb
import tkinter.ttk as ttk

from emulator.onemotion import OneMotion


class Windows:

    """
    GUI helps to set properties to ball
    """

    def __init__(self, master):
        class_name = self.__class__.__name__
        print(class_name, "Started")
        # Tk object instance
        self.master = master

        # Screen's size
        self.s_width = master.winfo_screenwidth()
        self.s_height = master.winfo_screenheight()
        # NoteBook dim
        self.n_width = round(self.s_width * 0.80)
        self.n_height = round(self.s_height * 0.80)
        # LabelFrame dim
        self.lf_width = round(self.s_width * 0.60)
        self.lf_height = round(self.s_height * 0.60)
        self.notebook = ttk.Notebook(
            self.master,
            width=self.n_width,
            height=self.n_height
        )
        self.labelvar1 = tk.StringVar()
        self.labelvar1.set('Common text')
        self.labelvar2 = tk.StringVar()
        self.labelvar2.set('Common text')
        self.labelvar3 = tk.StringVar()
        self.labelvar3.set('Common text')
        self.labelvar4 = tk.StringVar()
        self.labelvar4.set('Common text')
        # self.Ballconfig()
        self.notebook.pack()

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "Destroyed")

    def Ballconfig(self):
        self.frame1 = ttk.Frame(self.notebook)
        self.frame1.pack(fill=tk.BOTH, expand=True)
        self.notebook.add(self.frame1, text='Ball Settings')

        # LabelFrame1: Window
        self.labelframe1 = ttk.LabelFrame(self.frame1, text='Window')
        self.labelframe1.pack(fill=tk.BOTH, padx=5, pady=10, expand=False)
        # Width
        label1 = ttk.Label(self.labelframe1, textvariable=self.labelvar1)
        self.labelvar1.set(f'Ancho ventana max={self.s_width}')
        label1.pack(pady=50, padx=20, side='left')
        self.entry_w_width = ttk.Entry(self.labelframe1, justify=tk.LEFT)
        self.entry_w_width.pack(pady=50, padx=20, side='left')
        # Height
        label2 = ttk.Label(self.labelframe1, textvariable=self.labelvar2)
        self.labelvar2.set(f'Alto ventana max={self.s_height}')
        label2.pack(pady=50, padx=20, side='left')
        self.entry_w_height = ttk.Entry(self.labelframe1, justify=tk.LEFT)
        self.entry_w_height.pack(pady=50, padx=20, side='left')
        # Button
        self.button1 = Button(
            self.labelframe1,
            text='Guardar',
            command=self.setWin
        )
        self.button1.pack(padx=5, pady=5, side='left')

        # LabelFrame1: Window
        self.labelframe2 = ttk.LabelFrame(self.frame1, text='Ball')
        self.labelframe2.pack(fill=tk.BOTH, padx=5, pady=10, expand=True)

        # Select Sheet as main
        self.notebook.select(self.frame1)

    def setWin(self):
        width = self.entry_w_width.get()
        height = self.entry_w_height.get()
        if width != '' and height != '':
            mb.showinfo('Info', 'Valores cargados')
            # om = OneMotion(800, 500)
            om = OneMotion(int(width), int(height))
            om.main()
        else:
            mb.showerror('Error', 'Ambos valores son requeridos')
