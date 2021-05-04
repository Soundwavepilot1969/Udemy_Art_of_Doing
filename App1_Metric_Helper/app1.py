# Metric Helper app - Converts metric to imperial
import tkinter
from tkinter import IntVar, StringVar, ttk #ttk are more modern looking widgets but less customizable

#Define root window
root = tkinter.Tk()
root.config(bg="#7EC8E3")
root.title("Metric Helper")
# root.geometry("400x250") Not setting geometry - Tkinter will fit the widgets and autosize
root.resizable(0,0)

img = tkinter.PhotoImage(file=r"D:\All_Git_Projects\Udemy_Art_of_Doing\App1_Metric_Helper\wolf.png")
root.tk.call('wm', 'iconphoto', root._w, img)

# Define fonts and colors
field_font = ('Cambria', 10, 'bold')
bgcolor = "#0000FF"
buttoncolor = "#000C66"

#Define functions
def convert():
    '''Convert from metric to imperial'''
    condict = {
        'Millimeter':{'Inch':0.03937,'Foot':0.00328083333,'Yard':0.00109361111},
        'Centimeter':{'Inch':0.393700787,'Foot':0.032808399,'Yard':0.010936133},
        'Meter':{'Inch':39.3700787,'Foot':3.2808399,'Yard':1.0936133}
        }
    
    #Clear output field
    output_field.delete(0,"end")
    #Get user info
    input_value = float(input_field.get())
    input_metric = input_dropdown.get()
    output_imperial = output_dropdown.get()
    
    #Convert values using the dict
    final_value = input_value*condict[input_metric][output_imperial]
    output_field.insert(0,str(final_value))



#Define layout
main_frame = tkinter.LabelFrame(root, bg= bgcolor,width=300,height=100)
inner_frame = tkinter.Frame(main_frame, bg= bgcolor) #packing a frame within another frame to center contents

#Define widgets
input_field = tkinter.Entry(inner_frame, font = field_font, width = 20)
output_field = tkinter.Entry(inner_frame, font = field_font, width = 20)
equal_label = tkinter.Label(inner_frame, bg = bgcolor, text = "=", font = ('Cambria', 20, 'bold'), fg = "#FFFFFF")
submitbutton = tkinter.Button(inner_frame, bg = buttoncolor, text = "Convert", font = field_font, fg = "#FFFFFF", command = convert)

input_field.insert(0, 'Enter Input') #Enter this into the text box

input_field.grid(row = 0, column = 0, padx = 5, pady = 5, ipadx = 5, ipady = 5)
output_field.grid(row = 0, column = 2, padx = 5, pady = 5, ipadx = 5, ipady = 5)
equal_label.grid(row = 0, column = 1, padx = 5, pady = 5)
submitbutton.grid(row = 2, column = 0, columnspan=3, padx = 5, pady = (20,5), ipadx=30, ipady=5)

#create dropdowns
metric_list = ["Millimeter", "Centimeter", "Meter"]
imperial_list = ["Inch", "Foot", "Yard"]
# inputchoice = StringVar()
# outputchoice = StringVar()
# inputchoice.set('Millimeter')
# outputchoice.set('Inch') These are used only in case of OptionMenu in tkinter. For ttk combobox not required.

#input_dropdown = tkinter.OptionMenu(inner_frame, inputchoice, *metric_list) The asterisk unpacks the list
#output_dropdown = tkinter.OptionMenu(inner_frame, outputchoice, *imperial_list)

input_dropdown = ttk.Combobox(inner_frame,value=metric_list, font=field_font, justify = 'center')
output_dropdown = ttk.Combobox(inner_frame, values = imperial_list, font=field_font, justify = 'center')
input_dropdown.grid(row=1,column=0, ipadx = 5, ipady = 5)
output_dropdown.grid(row=1,column=2, ipadx = 5, ipady = 5)
input_dropdown.set('Millimeter')
output_dropdown.set('Inch')

# Packing frames 
main_frame.pack(padx=10, pady=10)
inner_frame.pack(padx=10, pady=(0,10))

#Running the root window loop
root.mainloop()