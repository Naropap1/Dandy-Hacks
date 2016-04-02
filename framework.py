# NapTimes 0.0.2
#
# Made entirely by Santiago Loane and nobody else at all
#
# #leggo #dandyhacks
#

#imports needed libraries, tkinter is the graphics & display tool
from tkinter import *
from tkinter import ttk
#from PIL import Image

#im = Image.open("images/pillow.png")

def sleep(*args):
	"Zzzz"

def pillow(*args):
#	im.show()
	"woo"

#beginning of a tkinter window
root = Tk()
root.title("NapTime bEtA")

#makes the primary display widget
mainframe = ttk.Frame(root, padding = "20 20 20 20")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(1,weight=1)

hours = StringVar()
time = StringVar()
hours_entry = ttk.Entry(mainframe, width=7, textvariable=hours)
hours_entry.grid(column=2, row=3, sticky=(W,E))
ttk.Label(mainframe, textvariable=time).grid(column=2, row=2, sticky=(W,E))
ttk.Button(mainframe, text="Nothing! Wow!", command=sleep).grid(column=3, row=3, sticky=W)

#Adds labels for each day of the week
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for i in range(0,len(weekdays)):
	ttk.Label(mainframe, text=weekdays[i]).grid(column=i+1, row=1, sticky=N)


ttk.Label(mainframe, text="Hours").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="you should").grid(column=2, row=2, sticky=E)
ttk.Label(mainframe, text="take a nap!").grid(column=3, row=2, sticky=W)

ttk.Button(mainframe, text = "Go to sleep now", command=pillow).grid(column=4, row=2, columnspan=2)

#image.grid(row=3, column=6, rowspan=2, columnspan=2, sticky = (N,E,S,W), padx=5, pady=5)

#adds extra padding for each element in grid
for child in mainframe.winfo_children():
	child.grid_configure(padx=5, pady=5)
#focus on the hours entered!
hours_entry.focus()
#also submit the form if they press enter, not just on button press
root.bind('<Return>', sleep)

#end of tkinter window
root.mainloop()