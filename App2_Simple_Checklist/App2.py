#Simple checklist app
import tkinter
from tkinter import ANCHOR,END

#Define root window
root = tkinter.Tk()
root.title('Simple Checklist')
root.config(bg="#FABEC0")
root.geometry('400x335')
root.resizable(0,0)

img = tkinter.PhotoImage(file=r"D:\All_Git_Projects\Udemy_Art_of_Doing\App2_Simple_Checklist\drop.png")
root.tk.call('wm','iconphoto', root._w, img)

# Define functions
def adding_item():
    '''Add item to list'''
    list_box.insert(END,enter_item.get())
    enter_item.delete(0,END)

def removing_item():
    '''Removed selected (ANCHOR) item from listbox'''
    list_box.delete(ANCHOR)
    enter_item.delete(0,END)

def clearing_list():
    '''Clear the listbox'''
    list_box.delete(0,END)
    enter_item.delete(0,END)

def saving_list():
    '''Save list to simple txt file'''
    with open(r'D:\All_Git_Projects\Udemy_Art_of_Doing\App2_Simple_Checklist\checklist.txt','w') as f:
        #listbox.get() returns a tuple
        list_tuple = list_box.get(0,END)
        for item in list_tuple:
            #include only one new line so that more \n is not added so use the if condition
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item+"\n")
        
def opening_list_ifthere(): #function that reads from saved file into the app if available
    try:
        with open(r'D:\All_Git_Projects\Udemy_Art_of_Doing\App2_Simple_Checklist\checklist.txt','r') as f:
            for line in f:
                list_box.insert(END,line)
    except:
        return

#Define Frames
input_frame = tkinter.LabelFrame(root, bg = "#F37970",width=400,height=50, text= "Enter List Item")
output_frame_1 = tkinter.Frame(root, bg = "#E43D40",width=400,height=228 )
output_frame_2 = tkinter.Frame(root, bg = "#E43D40", width=400, height=35)

#Define widgets
#For input frame
add_item = tkinter.Button(input_frame, text = "Add Item", bg = "#F85C70",activebackground="#F85C70", fg="#FFFFFF", command=adding_item)
enter_item = tkinter.Entry(input_frame, width = 40)
add_item.grid(row=0,column=5,padx=5,pady=(0,5),ipadx=25)
enter_item.grid(row=0,column=0,padx=5,pady=(0,5),columnspan=4,sticky='WE')

#For output frame 1
scroll_bar = tkinter.Scrollbar(output_frame_1) #scrollbar to scroll through list
list_box = tkinter.Listbox(output_frame_1, width = 59,bg="#F85C70", height=13, borderwidth=3, yscrollcommand=scroll_bar.set) #Adding listbox
list_box.grid(row=0,column=0,padx=(5,0),pady=5)
scroll_bar.config(command=list_box.yview)
scroll_bar.grid(row=0,column=1, sticky="NS",pady=5)

#For output frame 2
remove_item = tkinter.Button(output_frame_2, text = "Remove Item", bg = "#F85C70",activebackground="#F85C70", width=8, fg="#FFFFFF",command=removing_item)
clear_list = tkinter.Button(output_frame_2, text = "Clear List", bg = "#F85C70",activebackground="#F85C70", width=8, fg="#FFFFFF",command=clearing_list)
save_list = tkinter.Button(output_frame_2, text = "Save List", bg = "#F85C70",activebackground="#F85C70", width=8, fg="#FFFFFF", command=saving_list)
quit_list = tkinter.Button(output_frame_2, text = "Quit", bg = "#F85C70",activebackground="#F85C70", width=8, fg="#FFFFFF", command=root.destroy)
remove_item.grid(row=0,column=0,padx=5,pady=5,ipadx=10)
clear_list.grid(row=0,column=1,padx=5,pady=5,ipadx=10)
save_list.grid(row=0,column=2,padx=5,pady=5,ipadx=10)
quit_list.grid(row=0,column=3,padx=5,pady=5,ipadx=10)

#Pack Frames
input_frame.pack(padx=5,pady=5)
output_frame_1.pack(padx=5,pady=(0,5))
output_frame_2.pack(padx=5,pady=(0,5))
input_frame.grid_propagate(0)
output_frame_1.grid_propagate(0)
output_frame_2.grid_propagate(0)

#Calling the opening_list_ifthere function to open with the saved list
opening_list_ifthere()

#Running the root window loop
root.mainloop()