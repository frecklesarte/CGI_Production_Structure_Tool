import os
from os import path
from os.path import dirname, expanduser
import argparse

## Dynamically check the home directory on various operating systems..
class validate_home_directory(builtins.object):
    
    
    home = expanduser("~")
print(home, "\nHere is home directory")
    
