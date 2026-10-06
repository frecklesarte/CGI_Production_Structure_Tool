import os
from os import path
from os.path import expanduser
import pathlib as path

## Dynamically check the home directory on various operating systems..
 # Output: /home/username (Linux) or C:\Users\username(Windows)
class config_home_directory():
    home = expanduser("~")
    print(home)
    breakpoint()
    def user_home_directory():

        home = expanduser("~")
        print(home)
    breakpoint()
