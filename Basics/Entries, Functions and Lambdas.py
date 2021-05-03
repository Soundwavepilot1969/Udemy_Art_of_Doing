#Entries for user input and functions
import tkinter
root = tkinter.Tk()

root.title('Entries and Functions')
root.geometry('500x500')
root.config(bg='#FFA500')
root.resizable(0,0)

#Adding window icon
img = tkinter.PhotoImage(file="D:/All_Git_Projects/Udemy_Art_of_Doing/Basics/shield.png")
root.tk.call('wm', 'iconphoto', root._w, img)

# Defining function output that is called by the submit button
def print_output():
    '''Print the text entry in the output below'''
    text = tkinter.Label(output_frame, text=text_entry.get(), bg="#FF5C4D") 
    # get the input value from the text_entry entry widget and put it in as text for this label
    text.pack() #pack it into the output_frame
    text_entry.delete(0,"end") #delete the entered text from the entry box

# Defining the lambda function that counts on the screen on each click of count and also takes in the text entry
def count_up(number):
    '''Count up on the app'''
    global value # so that the value changes globally not just inside the function
    text = tkinter.Label(output_frame, text= str(number)+" "+text_entry.get(),bg = "#FF5C4D")
    text.pack()
    text_entry.delete(0,"end")
    value = number + 1

# Defining frames
input_frame=tkinter.Frame(root, bg = '#FFCD58',width=500, height=200)
output_frame=tkinter.Frame(root, bg='#FF5C4D', width=500, height=300)

# Packing frames onto root window
input_frame.pack(padx=10,pady=10)
output_frame.pack(padx=10,pady=(0,10)) #Can use fill and expand here to fill the window with the frame

# Add inputs
text_entry = tkinter.Entry(input_frame)
text_entry.grid(row=0, column=0,padx=5,pady=5)
input_frame.grid_propagate(0) #This is so that frame doesn't resize based on size of the text entry

submit_entry = tkinter.Button(input_frame, text = 'Submit', command=print_output)
# Submit button calls the print_output function defined above. 
# Here the print_output function is linked so no () used. For sending arguments use lambdas like below
submit_entry.grid(row=0, column=1,padx=5,pady=5)
input_frame.grid_propagate(0)

# Passing parameter with Lambda to the print_output function on the submit button click
value = 0
count_button = tkinter.Button(input_frame, text = 'Count', command=lambda:count_up(value))
count_button.grid(row=1,column=0,columnspan=2, padx=5, pady=5, sticky='WE')


#Keep output_frame size. Here pack is used as pack is used to put in the text entry to this frame
output_frame.pack_propagate(0)

# Running mainloop for root 
root.mainloop()