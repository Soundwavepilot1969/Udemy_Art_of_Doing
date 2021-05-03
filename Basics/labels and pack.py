import tkinter

root = tkinter.Tk()
root.title("Label Basics")
root.geometry("380x450")
root.resizable(0,0)
root.config(bg="#93e9be")

# Create label widget
name_label1 = tkinter.Label(root, text = 'Hello, My name is Ash.')
# Packing the label i.e. placing it in the window
name_label1.pack()

# Label 2 -> Pack just packs the label in and is one of the ways of adding a label into the root window
# The other way is using grids
name_label2 = tkinter.Label(root, text = 'Hello, My name is Ash2.',font = ('Arial', 18, 'bold'))
name_label2.pack()

name_label3 = tkinter.Label(root)
name_label3.config(text = "Using config to edit label") #can do above formatting this way too
name_label3.config(font=("cambria", 10))
name_label3.config(bg="#ff0000")
name_label3.pack(padx=10,pady=10) #Adding padding to the label

name_label4 = tkinter.Label(root, text='Hello, Goodevening', fg='blue')
name_label4.pack(padx=10,pady=(20,20),ipadx=50,ipady=50, anchor='e') 
#Internal padding and anchoring widget. e is for east

# filling entire space with label bg
name_label5 = tkinter.Label(root, text='This is label 5', fg='green')
name_label5.pack(fill = 'both', expand = True, padx=10,pady=10) #For fill you can type x, y or both





root.mainloop()