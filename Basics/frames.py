#Frames
# Use frames to organize and group widgets together
# Put other widgets into a frame and frame onto window

import tkinter

root = tkinter.Tk()
root.title("Frames")
root.config(bg="#7DF9FF")
root.geometry('500x500')

# You cannot use pack and grid together but can be used in separate frames
# Define frame 
pack_frame = tkinter.Frame(root, bg='red')
grid_frame = tkinter.Frame(root, bg='blue')
grid_frame2 = tkinter.LabelFrame(root, text = 'Label Frame', borderwidth=5)
# Pack frames on to root
pack_frame.pack(fill="both", expand=True, padx=20, pady=20)
grid_frame.pack(fill="both", expand=True, padx=20, pady=20)
grid_frame2.pack(fill="both", expand=True, padx=10, pady=10)


# Adding label into pack frame
name_label = tkinter.Label(pack_frame, text='Enter you name')
name_label.pack()
# Adding into grid frame 
name_button = tkinter.Button(grid_frame,text='Submit your name')
name_button.grid(row=0,column=0)
name_button1 = tkinter.Button(grid_frame,text='Submit your name1')
name_button1.grid(row=1,column=1)
name_button2 = tkinter.Button(grid_frame,text='Submit your name2')
name_button2.grid(row=2,column=2)

# Adding to grid frame 2
name_button3 = tkinter.Button(grid_frame2,text='AAAAAAAAAAAAAAAAAAAAAAAAAAAA')
name_button3.grid(row=0,column=0)

# run mainloop of root window
root.mainloop()