#Notepad App
import tkinter
from tkinter import END, LEFT, StringVar, IntVar, scrolledtext, messagebox, filedialog
from PIL import ImageTk, Image

#Define root window
root = tkinter.Tk()
root.config(bg="#738FA7")
root.title("Notepad App")
root.geometry("600x600")
root.resizable(0,0)

img = tkinter.PhotoImage(file=r"D:\All_Git_Projects\Udemy_Art_of_Doing\App4_Notepad\note.png")
root.tk.call('wm', 'iconphoto', root._w, img)

# Define functions
def change_font(event): #for optionmenu command = funtion automatically sends the selection to the function
    '''Get the font family, size and style'''
    if styles_Stringvar.get()=='none':
        myfont = (family_Stringvar.get(),sizes_Stringvar.get())
    else:
        myfont = (family_Stringvar.get(),sizes_Stringvar.get(), styles_Stringvar.get())
    input_text.config(font=myfont)

# Function for new note
def newnote():
    '''Empties the notepad'''
    # Before clearing notes create message box asking if you want to clear
    question = messagebox.askyesno('New Note','Are you sure you want to start a new note?')
    if question==1:
        input_text.delete(1.0,END) #Scrolled text starts at 1.0 not 0

# Function for asking message before closing window
def closenote():
    '''Closes notepad but asks message before doing so'''
    question = messagebox.askyesno('Close Notepad', 'Are you sure you want to quit?')
    if question==1:
        root.destroy()

#Function to save the note
def savenote():
    '''Save the note. First three lines saves the font family, size and style. Wont be shown in app'''
    # Use filedialog to get location and name to save file as
    save_name = filedialog.asksaveasfilename(initialdir="./", title='Save Note', filetypes=(("Text Files","*.txt"),("All Files","*.*")))
    with open(save_name,'w') as f:
        #First three lines are for fony family, size and style. Also size has to be string
        f.write(family_Stringvar.get()+"\n")
        f.write(str(sizes_Stringvar.get())+"\n")
        f.write(styles_Stringvar.get()+"\n")
        #write remaining text
        f.write(input_text.get(1.0,END))

#Function to open file
def opennote():
    '''Open a previously saved note. first set the font then load the text'''
    #Use filedialog to get location of note file
    open_name = filedialog.askopenfilename(initialdir="./", title='Open Note', filetypes=(("Text Files","*.txt"),("All Files","*.*")))
    with open(open_name,'r') as f:
        #Clear text
        input_text.delete(1.0,END)
        #First lines gives the font info. Strip the \n new line char at the end of each line
        family_Stringvar.set(f.readline().strip())
        sizes_Stringvar.set(int(f.readline().strip()))
        styles_Stringvar.set(f.readline().strip())

        #Call the change font for the font info and pass arbitrary value as this is a requirement of change font function due to the link to the optionmenu
        change_font(1)
        #read the rest of the file and insert into text field
        text = f.read()
        input_text.insert(1.0,text)
        
# Define Frames
button_frame = tkinter.LabelFrame(root, bg = "#0C4160")
input_frame = tkinter.LabelFrame(root, bg = "#738FA7")

# Definining and packing widgets

#Adding images
new_image=ImageTk.PhotoImage(Image.open(r'D:\All_Git_Projects\Udemy_Art_of_Doing\App4_Notepad\new.png'))
open_image=ImageTk.PhotoImage(Image.open(r'D:\All_Git_Projects\Udemy_Art_of_Doing\App4_Notepad\open.png'))
save_image=ImageTk.PhotoImage(Image.open(r'D:\All_Git_Projects\Udemy_Art_of_Doing\App4_Notepad\save.png'))
close_image=ImageTk.PhotoImage(Image.open(r'D:\All_Git_Projects\Udemy_Art_of_Doing\App4_Notepad\close.png'))


new_file = tkinter.Button(button_frame, bg = "#071330", fg="#FFFFFF",image=new_image, command=newnote)
open_file = tkinter.Button(button_frame, bg = "#071330", fg="#FFFFFF",image=open_image, command = opennote)
save_file = tkinter.Button(button_frame, bg = "#071330", fg="#FFFFFF",image=save_image,command=savenote)
close_file = tkinter.Button(button_frame, bg = "#071330", fg="#FFFFFF",image=close_image, command = closenote)

new_file.grid(row=0,column=1, padx=5, pady=5)
open_file.grid(row=0,column=2, padx=5, pady=5)
save_file.grid(row=0,column=3, padx=5, pady=5)
close_file.grid(row=0,column=4, padx=5, pady=5)

#List of font families
families = ['Terminal', 'Modern', 'Script', 'Courier', 'Arial', 'Calibri', 'Cambria', 'Georgia', 'MS Gothic', 'SimSun', 'Tahoma', 'Times New Roman', 'Verdana', 'Wingdings']
family_Stringvar= StringVar()
font_family = tkinter.OptionMenu(button_frame, family_Stringvar,*families, command = change_font)
family_Stringvar.set('Terminal')
# Set width to fit largest entry in list
font_family.config(width=16)

sizes = [8, 10, 12, 14, 16, 20, 24, 32, 48, 64, 72, 96]
sizes_Stringvar = IntVar()
font_size = tkinter.OptionMenu(button_frame, sizes_Stringvar, *sizes, command = change_font) #same change font command to get all options
sizes_Stringvar.set(12)
font_size.config(width=10)

styles = ['none', 'bold', 'italic']
styles_Stringvar = StringVar()
font_style = tkinter.OptionMenu(button_frame, styles_Stringvar, *styles, command = change_font)
styles_Stringvar.set('none')
font_style.config(width=10)

font_family.grid(row=0,column=5,padx=5,pady=5)
font_size.grid(row=0,column=6,padx=5,pady=5)
font_style.grid(row=0,column=7,padx=5,pady=5)


#Text frame
# Create the input area as a scrolltext to scroll through the text field
# Set the default width and height to be more than the root window size so tha the text field stays constant even on the smallest text size
myfont = (family_Stringvar.get(),sizes_Stringvar.get())
input_text = tkinter.scrolledtext.ScrolledText(input_frame, bg = "#C3CEDA", font = myfont, width=100,height=100)
input_text.pack()

# Packing Frames
button_frame.pack(padx=5,pady=5)
input_frame.pack(padx=5,pady=5)

# Running root window loop
root.mainloop()