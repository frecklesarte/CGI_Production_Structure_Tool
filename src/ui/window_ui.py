# Initializes the "tKinter" Python STL_UI module for creating the User Interface for the "DirectoryStructures" Pipeline Application
from tkinter import Tk
from tkinter import ttk


root = Tk()

# Setting the window properties
# Window Title
root.title("cgi_Production_Structure_Tool")
# Window background color
root.configure(background="grey24")
# Window Mix, Max Size specification
root.minsize(600, 400)
root.maxsize(1200, 1000)
# Sets the initial x, y size, as well as the x, y scale factor of the window
root.geometry("800x600+30+20")
# Boolean operation, Allow or Not Allow, scaling of x or y axis of 'root' window. Default x=False, y=False.
root.resizable(False, False)


# Creates the first 
frm = ttk.Frame(root, padding=10)
frm.grid()
# Assigns label objects to variables(ex.label1 = tk.label()).. then calls .pack() on the corresponding variable.
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

# Initializes the first label
ttk.Label(frm, text="Production Name").grid(column=0, row=0)
ttk.Entry = ttk.Label(frm, text="Enter, name of CGI Production", style="BW.TLabel").grid(column=1, row=0)
#productionDirectorylabel.pack()


#browseDirectorylabel = ttk.Label(root, text="Browse", style="BW.TLabel")
#browseDirectorylabel.pack()

#setDirectorylabel = ttk.Label(root, text="Specify, the TopLevel directory.", style="BW.TLabel")
# if 'browseDirectorylabel' is not 'specified' upon execution of 'createProductionStructurelabel'.. print(Root Production directory, 'not=>specified')     
#setDirectorylabel.pack()



## The final label which attempts to setup the creation of the "Production, Directory Structure." 
#createProductionStructurelabel = ttk.Label(root, text="Create if you must.", style="BW.TLabel")    
#createProductionStructurelabel.pack()

# Creates the button used to quit the application and deinitialize
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
# Create a check that makes sure the program frees from memory on the computer


 

root.mainloop()
