"""
# Author: Acxel Orozco
# Date: 22/09/2022
"""
import re


class InputVerify:

    """
    Utilities to verify input and entry
    """

    def __init__(self):
        class_name = self.__class__.__name__
        print(class_name, "Started")
        self.int_format = re.compile(r'^\-?[0-9][0-9]*$')
        '''
        ^: begin str
        "\"-?: negative or positive number
        [0-9][0-9]: first and next number can be 0-9
        $: str end
        '''

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "Destroyed")

    def Integer(self, text: str) -> bool:
        '''
        Verify int type number
        '''
        try:
            self.int_text = int(text)
        except ValueError:
            return False
        sting_is = re.match(self.int_format, text)
        if sting_is:
            return True
        else:
            return False
