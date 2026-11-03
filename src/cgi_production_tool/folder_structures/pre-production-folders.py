# Create a function that allows folders and sub-folders to be listed, and read here
import pathlib as Path

# Creates lists of all the folders required by pre-production
# Allow lists to be used for generating  preset folder-structures
#class list_preproduction_folders():

def list_top_folder():
# Lists the top-level-parent folder 'pre-production'.
    parent_folder = ['pre-production']
    print('parent_folder')
    # Lists  folders within  pre-production.
#def list_subfolders():
    
    subfolders = ['parent_folder', ['Research-Development'], ['Design'], ['Writing']]
    print('subfolders')
# List the subfolders and any sub-subfolders for pre-production.
#def list_subsubfolders():
