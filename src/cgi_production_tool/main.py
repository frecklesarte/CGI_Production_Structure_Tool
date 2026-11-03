#   This software is licensed as free and open-source through use of the GPL License
#   Authors: David Valencia (Freckles Arte) of Artist First Productions

from ui.main_window import root
from directory_generation.home_directory_validator import DirEntry
from folder_structures.pre_production_folders import preproduction_folders as preproduction
#from folder-structures.production-folders import list_production_folders
#from folder-structures.post-production-folders import list_postproduction_folders

class startup_application(root, DirEntry):

    print("packages are being loaded for the main application")

