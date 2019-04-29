# Import modules
# Numpy is module for numerical calculation.
# If you add 'as' after import, you can use the name you specified.

import numpy as np
from numpy import random


class AQUA:
    '''
    This is python class.
    '''

    def __init__(self, name, age, department):
        '''
        This is for initialize parameters called constructor.
        In python we usually use 'self' to specify its instance.
        '''
        self.name = name
        self.age = age
        self.department = department

    def information(self):
        '''
        This function is for printing members information.
        '''
        print("name:", self.name,
              "age:", self.age,
              "department:", self.department)

if __name__ == '__main__':
    # This is main part of program. This is like main function main().

    # Making instance of cocori
    cocori = AQUA('Ryosuke Satoh', 20, 'Environment and Information')

    # Printing my information.
    cocori.information()

    # Making instance of hoge
    hoge = AQUA('hoge', 100, 'Policy Management')
    hoge.information()
