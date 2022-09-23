"""
# Author: Acxel Orozco
# Date: 14/09/2022
"""

import tkinter as tk
from tkinter import Button
from tkinter import messagebox as mb
import tkinter.ttk as ttk

from emulator.onemotion import OneMotion
from emulator.mysprites.ball import Ball
from mycontrollers.io.inputverify import InputVerify


class Windows:

    """
    GUI helps to set properties to ball
    """

    def __init__(self, master):
        class_name = self.__class__.__name__
        print(class_name, "Started")
        # Tk object instance
        self.master = master

        # Text Verifier
        self.verify = InputVerify()

        # Collision info
        self.collision_info = {
            'screen_width': 0,
            'screen_height': 0
        }

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

        self.type_list = ['Simple', 'Multiple']

        # self.Ballconfig()
        self.notebook.pack()

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "Destroyed")

    def Ballconfig(self):
        '''
        Define screen size and other collision details
        '''
        self.frame1 = ttk.Frame(self.notebook)
        self.frame1.pack(fill=tk.BOTH, expand=True)
        self.notebook.add(self.frame1, text='General Settings')

        # LabelFrame1: Window
        self.labelframe1 = ttk.LabelFrame(self.frame1, text='Window')
        self.labelframe1.pack(fill=tk.BOTH, padx=5, pady=10, expand=False)
        # Width
        label1 = ttk.Label(self.labelframe1, textvariable=self.labelvar1)
        self.labelvar1.set(f'Window width max={self.s_width}')
        label1.pack(pady=50, padx=20, side='left')
        self.entry_w_width = ttk.Entry(self.labelframe1, justify=tk.LEFT)
        self.entry_w_width.pack(pady=50, padx=20, side='left')
        # Height
        label2 = ttk.Label(self.labelframe1, textvariable=self.labelvar2)
        self.labelvar2.set(f'Window height max={self.s_height}')
        label2.pack(pady=50, padx=20, side='left')
        self.entry_w_height = ttk.Entry(self.labelframe1, justify=tk.LEFT)
        self.entry_w_height.pack(pady=50, padx=20, side='left')
        # Button
        self.button_screen = Button(
            self.labelframe1,
            text='Save',
            command=self.setWin
        )
        self.button_screen.pack(padx=5, pady=5, side='left')

        # LabelFrame2: Ball
        self.labelframe2 = ttk.LabelFrame(self.frame1, text='Collision type')
        self.labelframe2.pack(fill=tk.BOTH, padx=5, pady=10, expand=False)
        # Collision type select
        self.coll_type = ttk.Combobox(self.labelframe2, values=self.type_list)
        self.coll_type.set('Select an option')
        self.coll_type.pack(padx=5, pady=5, side='left')
        # Button
        self.button_type = Button(
            self.labelframe2,
            text='Ok',
            command=self.setType
        )
        self.button_type.pack(padx=5, pady=5, side='left')
        self.button_type.config(state=tk.DISABLED)

        # Frame2: sheet2
        self.frame2 = ttk.Frame(self.notebook)
        self.frame2.pack(fill=tk.BOTH, expand=True)
        self.notebook.add(self.frame2, text='Collision Settings')

        # Select Sheet as main
        self.notebook.select(self.frame1)

    def setWin(self):
        width = self.entry_w_width.get()
        height = self.entry_w_height.get()
        if width != '' and height != '':
            if self.verify.Integer(height) and self.verify.Integer(width):
                my_height = int(height)
                my_width = int(width)

                if my_height < self.s_height and my_width < self.s_width:
                    mb.showinfo('Info', 'Saved')

                    # Save info
                    self.collision_info['screen_width'] = my_width
                    self.collision_info['screen_height'] = my_height

                    # Entry and button disabled
                    self.entry_w_height.config(state=tk.DISABLED)
                    self.entry_w_width.config(state=tk.DISABLED)
                    self.button_screen.config(state=tk.DISABLED)
                    self.button_type.config(state=tk.NORMAL)

                else:
                    mb.showerror(
                        'Error',
                        'Values close to screen dimension'
                    )
            else:
                mb.showerror('Error', 'Only integer values are allowed')
        else:
            mb.showerror('Error', 'All values are required')

    def setType(self):
        if self.coll_type.get() == 'Simple':
            om = OneMotion(
                self.collision_info['screen_width'],
                self.collision_info['screen_height']
            )
            om.main()
        if self.coll_type.get() == 'Multiple':
            mb.showinfo('Info', 'Multiple selected')
