# Initializes the "tKinter" Python STL_UI module for creating the User Interface for the "DirectoryStructures" Pipeline Application
from tkinter import Tk
from tkinter import ttk
from ui.frame_production_name import create_production_name

root = Tk()

# Setting the window properties
# Window Title
# Window background color
# Window Min, Max Sizing config
# Initial x, y size, as well as the x, y scale factor of the window.
# Boolean Operation, Allow or Disallow, scaling of x or y axis of 'root' window.
# Default x=True, y=True
root.title("cgi_Production_Structure_Tool")
root.configure(background="grey24")
root.minsize(600, 400)
root.maxsize(1200, 1000)
root.geometry("800x600+30+20")
root.resizable(True, True)

# Define a function which draws all frames from imported packages
def draw_frames():
# What does this create specifically again? A frame, with a grid it seems like
frm = ttk.Frame(root, padding=10)
frm.grid()
# Defines Style configs to variables
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

# Initializes the first label
ttk.Label(frm, text="Production Name").grid(column=0, row=0)
ttk.Entry = ttk.Label(frm, text='Enter, name of CGI Production', style="BW.TLabel").grid(column=1, row=0)
#productionDirectorylabel.pack()


#browseDirectorylabel = ttk.Label(root, text="Browse", style="BW.TLabel")
#browseDirectorylabel.pack()

#setDirectorylabel = ttk.Label(root, text="Specify, the TopLevel directory.", style="BW.TLabel")
# if 'browseDirectorylabel' is not 'specified' upon execution of 'createProductionStructurelabel'.. print(Root Production directory, 'not=>specified')     
#setDirectorylabel.pack()



## The final label which attempts to setup the creation of the "Production, Directory Structure." 

# Creates the button used to quit the application and deinitialize
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
# Create a check that makes sure the program frees from memory on the computer


 

root.mainloop()
