# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# imports
import sys
import numpy as np
import matplotlib.pyplot as plt


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


import perceptron as p

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    perceptron = p.Perceptron(10)
    output = perceptron.sigmoid()
    print(output)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
