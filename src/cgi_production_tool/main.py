import os
from os import path
from os.path import dirname, expanduser
import pathlib as path

## Dynamically check the home directory on various operating systems..
 # Output: /home/username (Linux) or C:\Users\username(Windows)
class check_home_directory():

    home = expanduser("~")

    print(home)
