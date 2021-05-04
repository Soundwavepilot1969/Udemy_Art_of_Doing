#GUI_World app
import tkinter
from tkinter import IntVar, StringVar
from PIL import ImageTk, Image

#Define root window
root = tkinter.Tk()
root.config(bg="#FF8300")
root.title("GUI World")
root.geometry("400x400")
root.resizable(0,0)

img = tkinter.PhotoImage(file=r"D:\All_Git_Projects\Udemy_Art_of_Doing\App0_GUI_World\bug.png")
root.tk.call('wm', 'iconphoto', root._w, img)

#Define functions
def submit_name():
    '''Say hello to user'''
    global optionnum
    if optionnum.get()=='normal':
        output_text = tkinter.Label(output_frame, text="Hello "+textbox.get()+". Welcome to the World!!!", bg = "#DF362D", fg = "#FFFFFF")
    elif optionnum.get()=='upper':
        output_text = tkinter.Label(output_frame, text=("Hello "+textbox.get()+". Welcome to the World!!!").upper(), bg = "#DF362D", fg = "#FFFFFF")
    output_text.pack()
    textbox.delete(0,"end")

#Define and Pack Frames
input_frame = tkinter.LabelFrame(root, bg="#FF4500",width=300,height=100)
input_frame_in = tkinter.Frame(input_frame, bg="#FF4500") #packing a frame within another frame to center contents
output_frame = tkinter.Frame(root, bg="#DF362D",width=500,height=300)
input_frame.pack(padx=10, pady=10)
output_frame.pack(padx=10, pady=(0,10))

#Define widgets for inputframe
textbox = tkinter.Entry(input_frame_in)
textbox.grid(row=0,column=0,padx=5,pady=5)
submit_button = tkinter.Button(input_frame_in, text='Submit', command = submit_name)
submit_button.grid(row=0,column=1,padx=5,pady=5, ipadx=20)
optionnum = StringVar()
optionnum.set('normal')
option_1 = tkinter.Radiobutton(input_frame_in, text='Normal Case', variable = optionnum, value = 'normal', bg = "#FF4500", activebackground = "#FF4500")
option_2 = tkinter.Radiobutton(input_frame_in, text='UPPER Case', variable = optionnum, value = 'upper', bg = "#FF4500", activebackground = "#FF4500")
option_1.grid(row=1,column=0)
option_2.grid(row=1,column=1)
input_frame_in.pack(pady=15)

#Define widgets for outputframe
img2 = ImageTk.PhotoImage(file=r"D:\All_Git_Projects\Udemy_Art_of_Doing\App0_GUI_World\smile.png")
output_label = tkinter.Label(output_frame, image= img2, bg = "#DF362D")
output_label.pack()


#retain size of frames
input_frame.pack_propagate(0)
output_frame.pack_propagate(0)

#Running the root window loop
root.mainloop()