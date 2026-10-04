import os
from os import path
from os.path import expanduser

## Dynamically check the home directory on various operating systems..

home = expanduser("~")

print(home)
# Output: /home/username (Linux) or C:\Users\username (Windows)
