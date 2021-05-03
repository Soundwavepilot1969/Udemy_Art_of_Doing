# Images
# putting images is a multistep process. Need to create image first and 
# then put it on some widget and then put that widget onto the screen
import tkinter
from PIL import ImageTk, Image #For working with jpeg files

# Define window
root = tkinter.Tk()
root.config(bg='#D4F1F4')
root.title('Image Basics')
root.geometry('500x500')
img = tkinter.PhotoImage(file='D:/All_Git_Projects/Udemy_Art_of_Doing/Basics/fight.png')
root.tk.call('wm', 'iconphoto', root._w, img)
root.resizable(0,0)

# Define functions
def make_image():
    global jpimage #Image should be set as global variable for it to get displayed from within a function
    # For working with jpeg files you need additional libraries. Pillow needs to be installed
    jpimage = ImageTk.PhotoImage(Image.open('D:/All_Git_Projects/Udemy_Art_of_Doing/Basics/dog.jpg').resize((260,300),Image.ANTIALIAS))
    # Using pillow and image to work with jpeg files
    dog_label = tkinter.Label(root, image = jpimage)
    dog_label.pack()



# For png files
my_img = tkinter.PhotoImage(file='D:/All_Git_Projects/Udemy_Art_of_Doing/Basics/finder.png')
my_label = tkinter.Label(root, image = my_img)
my_label.pack()

my_button = tkinter.Button(root,text = 'Who let the dogs out', command=make_image) #can add the image to any widget
my_button.pack()



# Running the root window loop
root.mainloop()