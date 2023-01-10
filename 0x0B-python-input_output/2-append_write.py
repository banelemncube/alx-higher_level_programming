#!/usr/bin/python3
"""defines a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
"""appends string to text file"""
    with open(filename, 'a') as f:
        return f.write(text)
