#Color Theme Maker app
import tkinter
from tkinter import BOTH, IntVar, DISABLED, filedialog

#Define root window
root = tkinter.Tk()
root.config(bg="#B7CFDC")
root.title("Color Theme Maker")
# root.geometry("500x500")
root.resizable(0,0)

img = tkinter.PhotoImage(file=r"D:\All_Git_Projects\Udemy_Art_of_Doing\App5_Color_Theme_Maker\colo.png")
root.tk.call('wm', 'iconphoto', root._w, img)

#Define functions
def get_red(sliderval):
    '''gets slider value of red and turns in hex and updates color. The scale value is passed automatically when the scale is moved calling this function'''
    global red_value

    #turn slider vlaue into into and hex and strip leading characters
    red_value = hex(int(sliderval))
    red_value=red_value.lstrip("0x")

    #if hex value is single digit then lead with a 0 such that d becomes 0d
    while len(red_value)<2:
        red_value="0"+str(red_value)

    update_color()

def get_green(sliderval):
    '''gets slider value of green and turns in hex and updates color. The scale value is passed automatically when the scale is moved calling this function'''
    global green_value
    green_value = hex(int(sliderval))
    green_value=green_value.lstrip("0x")
    while len(green_value)<2:
        green_value="0"+str(green_value)
    update_color()

def get_blue(sliderval):
    '''gets slider value of green and turns in hex and updates color. The scale value is passed automatically when the scale is moved calling this function'''
    global blue_value
    blue_value = hex(int(sliderval))
    blue_value=blue_value.lstrip("0x")
    while len(blue_value)<2:
        blue_value="0"+str(blue_value)
    update_color()

def update_color():
    '''Updates the color box and labels for the selected color based on hex value'''
    color_box = tkinter.Label(input_frame, bg="#"+red_value+green_value+blue_value, height=6, width=15)
    color_box.grid(row=1,column=3,columnspan=2,padx=35,pady=10)

    #Change the labels to reflect selected color
    color_tuple.config(text='(' + str(red_slider.get()) + '),' + '(' + str(green_slider.get()) + '),' + '(' + str(blue_slider.get()) + ')')
    color_hex.config(text="#" + red_value + green_value + blue_value)

def set_color(r,g,b):
    '''Update to clicked color'''
    red_slider.set(r)
    green_slider.set(g)
    blue_slider.set(b)

def stores_color():
    global stored_colors
    '''Store the current color tuple value to display color'''
    #get current value of each slider and appen 0s to keep formatting consistent
    red=str(red_slider.get())
    while len(red)<3:
        red='0'+red

    green=str(green_slider.get())
    while len(green)<3:
        green='0'+green

    blue=str(blue_slider.get())
    while len(blue)<3:
        blue='0'+blue

    #Keep a reference of current color
    stored_red = red_slider.get()
    stored_green = green_slider.get()
    stored_blue = blue_slider.get()

    #Create new widgets to store the color. This is the approach in the tutorial but can be done by updating too
    recall_button = tkinter.Button(output_frame, text = ' Recall Color', command = lambda:set_color(stored_red,stored_green,stored_blue))
    recall_color_tuple = tkinter.Label(output_frame, text='(' + red + '),' + '(' + green + '),' + '(' + blue + ')')
    recall_color_hex = tkinter.Label(output_frame, text ="#" + red_value + green_value + blue_value)
    recall_color_boxframe = tkinter.Label(output_frame,bg='black',width=3,height=1)
    recall_color_box = tkinter.Label(output_frame,bg="#" + red_value + green_value + blue_value, width=3, height=1)

    #Put new widgets on the screen
    recall_button.grid(row=stored_color.get(),column=1, padx=20)
    recall_color_tuple.grid(row=stored_color.get(),column=2, padx=20)
    recall_color_hex.grid(row=stored_color.get(),column=3, padx=20)
    recall_color_boxframe.grid(row=stored_color.get(),column=4,pady=2,ipadx=3,ipady=3)
    recall_color_box.grid(row=stored_color.get(),column=4)

    # Updating the dictionary stored_colors
    stored_colors[stored_color.get()]=[recall_color_tuple.cget("text"),recall_color_hex.cget("text")]

    # Move the radio button to next value if available
    if stored_color.get()<5:
        stored_color.set(stored_color.get()+1)

def save_colors():
    '''Saves the colors to a text file''' #Additional something that can be done is calling this back into stored_colors on opening
    saved_colors = filedialog.asksaveasfilename(initialdir="./", title='Save Colors', filetypes=(("Text Files","*.txt"),("All Files","*.*")))
    with open(saved_colors,'w') as f:
        f.write("Color Theme Maker Output - \n")
        for saved_entry in stored_colors.values():
            f.write(saved_entry[0]+'\n'+saved_entry[1]+'\n\n')

#Define Layout
input_frame = tkinter.LabelFrame(root, bg="#D9E4EC",padx=5,pady=5) #Padding applied here and not when packing
output_frame = tkinter.LabelFrame(root,bg="#D9E4EC",padx=5,pady=5)

#Widgets for input frame
#Sliders for each RGB color
red_label = tkinter.Label(input_frame, text="R",bg='#D9E4EC')
red_slider = tkinter.Scale(input_frame, from_=0, to=255, command=get_red) #Scale for sliders. its from_ not from
red_button = tkinter.Button(input_frame, text="Red", command = lambda:set_color(255,0,0))
green_label = tkinter.Label(input_frame, text="G",bg='#D9E4EC')
green_slider = tkinter.Scale(input_frame, from_=0, to=255, command = get_green)
green_button = tkinter.Button(input_frame, text="Green", command = lambda:set_color(0,255,0))
blue_label = tkinter.Label(input_frame, text="B",bg='#D9E4EC')
blue_slider = tkinter.Scale(input_frame, from_=0, to=255,command = get_blue)
blue_button = tkinter.Button(input_frame, text="Blue", command = lambda:set_color(0,0,255))

#Create buttons for complementary colors CMY
yellow_button = tkinter.Button(input_frame, text="Yellow", command = lambda:set_color(255,255,0))
cyan_button = tkinter.Button(input_frame, text="Cyan", command = lambda:set_color(0,255,255))
magenta_button = tkinter.Button(input_frame, text="Magenta", command = lambda:set_color(255,0,255))

#Create utility buttons
store_color = tkinter.Button(input_frame,text = "Store Color", command = stores_color)
save_button = tkinter.Button(input_frame, text = "Save", command=save_colors)
quit_button = tkinter.Button(input_frame,text="Quit", command=root.destroy)

# Packing widgets onto frame
red_label.grid(row=0,column=0,sticky='W')
red_slider.grid(row=1,column=0,sticky='W',pady=1)
red_button.grid(row=2,column=0,ipadx=20,padx=1,pady=1)

green_label.grid(row=0,column=1,sticky='W')
green_slider.grid(row=1,column=1,sticky='W',pady=1)
green_button.grid(row=2,column=1,ipadx=20,padx=1,pady=1)

blue_label.grid(row=0,column=2,sticky='W')
blue_slider.grid(row=1,column=2,sticky='W',pady=1)
blue_button.grid(row=2,column=2,ipadx=20,padx=1,pady=1)

yellow_button.grid(row=3,column=0,padx=1,pady=1,sticky='WE')
cyan_button.grid(row=3,column=1,padx=1,pady=1,sticky='WE')
magenta_button.grid(row=3,column=2,padx=1,pady=1,sticky='WE')

store_color.grid(row=4,column=0,columnspan=3,sticky='WE')
save_button.grid(row=4,column=3, sticky='WE')
quit_button.grid(row=4,column=4, sticky='WE')

# Create colorbox and color labels
color_box = tkinter.Label(input_frame,bg='black', height=6, width=15)
color_tuple = tkinter.Label(input_frame, text='(0),(0),(0)',bg="#D9E4EC")
color_hex = tkinter.Label(input_frame, text='#000000',bg="#D9E4EC")
color_box.grid(row=1,column=3,columnspan=2,padx=35,pady=10,ipadx=10,ipady=10)
color_tuple.grid(row=2,column=3,columnspan=2)
color_hex.grid(row=3,column=3,columnspan=2)

#Widgets for output frame
#initialize dictionary to store all the colors
stored_colors={}
stored_color=IntVar() #This variable keeps track of which row is selected (value of i from radiobutton)

#Create radio buttons to select stored colors and populate each row with placeholder values. For loop used
for i in range(6):
    radio_button = tkinter.Radiobutton(output_frame, variable=stored_color,value=i)
    radio_button.grid(row=i,column=0,sticky='W')

    recall_button = tkinter.Button(output_frame, text='Recall Color', state=DISABLED)
    new_color_tuple = tkinter.Label(output_frame, text='(255), (255), (255)')
    new_color_hex = tkinter.Label(output_frame,text='#FFFFFF')
    new_color_boxframe = tkinter.Label(output_frame,bg='black',width=3,height=1)
    new_color_box = tkinter.Label(output_frame,bg='white', width=3, height=1)

    recall_button.grid(row=i,column=1, padx=20)
    new_color_tuple.grid(row=i,column=2, padx=20)
    new_color_hex.grid(row=i,column=3, padx=20)
    new_color_boxframe.grid(row=i,column=4,pady=2,ipadx=3,ipady=3)
    new_color_box.grid(row=i,column=4)

    #.cget() function returns the value of  specific option. Store the text value of the tuple label and hex label
    stored_colors[stored_color.get()]=[new_color_tuple.cget('text'),new_color_hex.cget('text')]


# Packing Frames
input_frame.pack(padx=5,pady=5,fill=BOTH,expand=True)
output_frame.pack(padx=5,pady=(0,5),fill=BOTH,expand=True)


#Initialize starting colors for the color box so that not defined error is removed. global variable set within function reason for this
red_value="00"
green_value="00"
blue_value="00"

# Running root window loop
root.mainloop()