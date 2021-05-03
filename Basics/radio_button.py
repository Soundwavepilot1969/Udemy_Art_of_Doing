# Radio Button

import tkinter
from tkinter import IntVar, StringVar #These are used to track the radio button clicks
# Define window
root = tkinter.Tk()
root.config(bg='#B2D2A4')
root.title('Radio Buttons')
root.geometry('500x500')
img = tkinter.PhotoImage(file='D:/All_Git_Projects/Udemy_Art_of_Doing/Basics/shield.png')
root.tk.call('wm', 'iconphoto', root._w, img)
root.resizable(0,0)

# Defining functions
def make_label():
    '''Print to the screen based on input from radio button'''
    if number.get() == 1:
        num_label = tkinter.Label(output_frame, text = "Option 1 selected")
    elif number.get() == 2:
        num_label = tkinter.Label(output_frame, text = "Option 2 selected")
    num_label.pack()

# Defining frames
input_frame=tkinter.LabelFrame(root, bg = '#B2D2A4',width=500, height=200, text = 'Label_Here')
output_frame=tkinter.Frame(root, bg='#2C5E1A', width=500, height=300)
# Packing frames onto root window
input_frame.pack(padx=10,pady=10)
output_frame.pack(padx=10,pady=(0,10))

# Create Radio Buttons
number = IntVar() #This will track the radio button clicks
number.set(1) #Sets initial value to 1 so 1st option selected
radio_1 = tkinter.Radiobutton(input_frame, text = 'Option 1', variable = number, value = 1) #Radio buttons tracked using variable number defined above
radio_2 = tkinter.Radiobutton(input_frame, text = 'Option 2', variable = number, value = 2)
print_button = tkinter.Button(input_frame, text = "Print Output", command=make_label)
#Packing buttons onto frames
radio_1.grid(row=0,column=0,padx=10,pady=10)
radio_2.grid(row=1,column=0,padx=10,pady=10)
print_button.grid(row=0,column=1,padx=10,pady=10, rowspan=2, sticky='NS')

# Running the root window
root.mainloop()