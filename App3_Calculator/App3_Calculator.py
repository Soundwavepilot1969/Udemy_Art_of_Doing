#Calculator App
import tkinter
from tkinter import RIGHT, END, DISABLED, NORMAL
#Define root window
root = tkinter.Tk()
root.config(bg="#D6AD60")
root.title("Calculator")
root.geometry("300x390")
root.resizable(0,0)

img = tkinter.PhotoImage(file=r"D:\All_Git_Projects\Udemy_Art_of_Doing\App3_Calculator\calc.png")
root.tk.call('wm', 'iconphoto', root._w, img)

button_font = ('Arial',18)
display_font = ('Arial', 30)

#Define functions

# Function to get input 
def submit_number(number):
    '''Submit number or decimal point to end of display'''
    entry_box.insert(END, number)

    # If decimal already entered disable decimal point button
    if '.' in entry_box.get():
        decimal_button.config(state=DISABLED)

# Function to get operator used and store first entry
def operate(operator):
    '''Store the first number and operation to be used'''
    global first_number
    global operation

    # Get first number and operator
    first_number=entry_box.get()
    operation=operator

    # Delete first number from display
    entry_box.delete(0,END)

    # Disable all operator until equal or clear is pressed
    add_button.config(state=DISABLED)
    subtract_button.config(state=DISABLED)
    multiply_button.config(state=DISABLED)
    divide_button.config(state=DISABLED)
    exponent_button.config(state=DISABLED)
    inverse_button.config(state=DISABLED)
    square_button.config(state=DISABLED)

    #Return decimal to normal so that it can be added to second number if needed
    decimal_button.config(state=NORMAL)

# Function to enable buttons
def enable_button():
    '''Enable all buttons'''
    add_button.config(state=NORMAL)
    subtract_button.config(state=NORMAL)
    multiply_button.config(state=NORMAL)
    divide_button.config(state=NORMAL)
    exponent_button.config(state=NORMAL)
    inverse_button.config(state=NORMAL)
    square_button.config(state=NORMAL)
    decimal_button.config(state=NORMAL)

# Function to perform operation
def equal():
    '''Run stored operation for two numbers'''
    if operation =='add':
        value = float(first_number)+float(entry_box.get())
    elif operation=='subtract':
        value = float(first_number)-float(entry_box.get())
    elif operation=='multiply':
        value = float(first_number)*float(entry_box.get())
    elif operation=='divide':
        if entry_box.get()=='0':
            value = 'ERROR'
        else:
            value = float(first_number)/float(entry_box.get())
    elif operation=='exponent':
        value = float(first_number)**float(entry_box.get())
    
    #Remove current value in display and display output
    entry_box.delete(0,END)
    entry_box.insert(0,value)

    # Return buttons to normal state
    enable_button()

# Function to clear display
def clear():
    '''Clear everything'''
    entry_box.delete(0,END)
    enable_button()

# Inverse function
def inverse():
    '''Calculate inverse of function'''
    if entry_box.get()=='0':
        value='ERROR'
    else:
        value=1/float(entry_box.get())
        # Remove entry in display and update
        entry_box.delete(0,END)
        entry_box.insert(0,value)

# Square function
def squared():
    '''Squares the entry'''
    value=float(entry_box.get())**2
    entry_box.delete(0,END)
    entry_box.insert(0,value)

#Negate function
def negate():
    '''Negate the number'''
    value=float(entry_box.get())*-1
    entry_box.delete(0,END)
    entry_box.insert(0,value)

#Define Frames
output_frame = tkinter.LabelFrame(root, bg = "#122620")
input_frame = tkinter.LabelFrame(root, bg = "#D6AD60")

# Definining and packing widgets
entry_box = tkinter.Entry(output_frame,borderwidth=1, font = display_font, bg = "#F4EBD0", width=50, justify=RIGHT)
entry_box.pack()

#Button widgets
clear_button = tkinter.Button(input_frame, bg = "#122620", fg="#FFFFFF", text = "Clear", font = button_font, command=clear)
quit_button = tkinter.Button(input_frame, bg = "#122620", fg="#FFFFFF", text = "Quit", font = button_font, command = root.destroy)

inverse_button = tkinter.Button(input_frame, text='1/x', bg = "#122620", fg="#FFFFFF", font = button_font, command = inverse)
square_button = tkinter.Button(input_frame, text='x^2', bg = "#122620", fg="#FFFFFF", font = button_font, command = squared)
exponent_button = tkinter.Button(input_frame, text='x^n', bg = "#122620", fg="#FFFFFF", font = button_font, command = lambda:operate('exponent'))
divide_button = tkinter.Button(input_frame, text='/', bg = "#122620", fg="#FFFFFF", font = button_font, command = lambda:operate('divide'))
multiply_button = tkinter.Button(input_frame, text='*', bg = "#122620", fg="#FFFFFF", font = button_font, command = lambda:operate('multiply'))
subtract_button = tkinter.Button(input_frame, text='-', bg = "#122620", fg="#FFFFFF", font = button_font, command = lambda:operate('subtract'))
add_button = tkinter.Button(input_frame, text='+', bg = "#122620", fg="#FFFFFF", font = button_font, command = lambda:operate('add'))
equal_button = tkinter.Button(input_frame, text='=', bg = "#122620", fg="#FFFFFF", font = button_font, command = equal)
decimal_button = tkinter.Button(input_frame, text='.', bg = "#122620", fg="#FFFFFF", font = button_font, command=lambda:submit_number('.'))
negate_button = tkinter.Button(input_frame, text='+/-', bg = "#122620", fg="#FFFFFF", font = button_font, command = negate)


nine_button = tkinter.Button(input_frame, text='9', bg = 'black', fg='white', font = button_font, command=lambda:submit_number(9))
eight_button = tkinter.Button(input_frame, text='8', bg = 'black', fg='white', font = button_font, command=lambda:submit_number(8))
seven_button = tkinter.Button(input_frame, text='7', bg = 'black', fg='white', font = button_font, command=lambda:submit_number(7))
six_button = tkinter.Button(input_frame, text='6', bg = 'black', fg='white', font = button_font, command=lambda:submit_number(6))
five_button = tkinter.Button(input_frame, text='5', bg = 'black', fg='white', font = button_font, command=lambda:submit_number(5))
four_button = tkinter.Button(input_frame, text='4', bg = 'black', fg='white', font = button_font, command=lambda:submit_number(4))
three_button = tkinter.Button(input_frame, text='3', bg = 'black', fg='white', font = button_font, command=lambda:submit_number(3))
two_button = tkinter.Button(input_frame, text='2', bg = 'black', fg='white', font = button_font, command=lambda:submit_number(2))
one_button = tkinter.Button(input_frame, text='1', bg = 'black', fg='white', font = button_font, command=lambda:submit_number(1))
zero_button = tkinter.Button(input_frame, text='0', bg = 'black', fg='white', font = button_font, command=lambda:submit_number(0))

# Row 1
clear_button.grid(row=0,column=0,columnspan=2,sticky="WE")
quit_button.grid(row=0,column=2,columnspan=2,sticky="WE")
#Row 2
inverse_button.grid(row=1,column=0, pady=1, sticky='WE')
square_button.grid(row=1,column=1, pady=1, sticky='WE')
exponent_button.grid(row=1,column=2, pady=1, sticky='WE')
divide_button.grid(row=1,column=3, pady=1, sticky='WE')
# Row 3 Add padding to create size of column. Size defined by largest widget so add enough padding to make all equal
seven_button.grid(row=2,column=0, pady=1, sticky='WE', ipadx=20)
eight_button.grid(row=2,column=1, pady=1, sticky='WE', ipadx=20)
nine_button.grid(row=2,column=2, pady=1, sticky='WE', ipadx=20)
multiply_button.grid(row=2,column=3, pady=1, sticky='WE', ipadx=20)
# Row 4
four_button.grid(row=3,column=0, pady=1, sticky='WE')
five_button.grid(row=3,column=1, pady=1, sticky='WE')
six_button.grid(row=3,column=2, pady=1, sticky='WE')
subtract_button.grid(row=3,column=3, pady=1, sticky='WE')
# Row 5
one_button.grid(row=4,column=0, pady=1, sticky='WE')
two_button.grid(row=4,column=1, pady=1, sticky='WE')
three_button.grid(row=4,column=2, pady=1, sticky='WE')
add_button.grid(row=4,column=3, pady=1, sticky='WE')
# Row 6
negate_button.grid(row=5,column=0, pady=1, sticky='WE')
zero_button.grid(row=5,column=1, pady=1, sticky='WE')
decimal_button.grid(row=5,column=2, pady=1, sticky='WE')
equal_button.grid(row=5,column=3, pady=1, sticky='WE')

# Packing Frames
output_frame.pack(padx=2,pady=(5,20))
input_frame.pack(padx=2,pady=5)


#Running root window loop
root.mainloop()