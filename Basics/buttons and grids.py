#Buttons and Grids
#Grid system for placement of widgets. Better than pack

import tkinter

root = tkinter.Tk()
root.title('Buttons and Grids')
root.geometry('500x500')
root.resizable(0,0)

name_button = tkinter.Button(root, text='Name')
name_button.grid(row=0, column=0) #Rows and columns are defined on the fly

time_button = tkinter.Button(root, text='Time')
time_button.grid(row=1, column=1)

place_button = tkinter.Button(root, text='Place', bg="#00ffff", activebackground='#ff0000')
place_button.grid(row=2,column=2, padx=10, pady=10,ipadx=15) #Setting background, padding and when clicking bg color

day_button = tkinter.Button(root, text = 'Day', bg='white', borderwidth=5)
day_button.grid(row=3,column=0,columnspan=3,sticky='WE') #Spanning the button across 3 columns. WE for west to east

# The size of the columns are defined by the largest item in the column. 
# This is the reason for the odd spacing. Solution to this in later files

# Calling root
root.mainloop()