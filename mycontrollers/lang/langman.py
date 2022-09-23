"""
# Author: Acxel Orozco
# Date: 22/09/2022
"""

import json
from tkinter import messagebox as mb


class LangManager:

    '''
    Get langdictionary
    '''

    def __init__(self):
        class_name = self.__class__.__name__
        print(class_name, "Started")

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "Destroyed")

    def getLang(self):
        try:
            with open("lang.json") as file:
                data = json.load(file)
                return data
        except ValueError:
            mb.showerror('Error', 'Problem load langdictionary')
