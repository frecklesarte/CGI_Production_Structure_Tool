## Dynamically check the home directory on various operating systems..
import os
from os import path
from os.path import expanduser

home = expanduser("~")
print(home) # Output: /home/username (Linux) or C:\Users\username (Windows)
