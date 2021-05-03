# windows basics
import tkinter

# Create a top level root widget that is going to be root window of app. Its a container for other widgets
root = tkinter.Tk()
root.title('Window Basics')
root.geometry("600x480+100+100") #Sets the size of the window and also the +100+100 for positioning on screen
root.resizable(1,1) #won't be able to resize window if 0,0
root.config(bg='#AEC6CF') #Sets window bg to color of this hex value
# root.iconbitmap(r"magic.ico") -> This doesn't work. Maybe cos of the ico file format???

img = tkinter.PhotoImage(file="D:/All_Git_Projects/Udemy_Art_of_Doing/Basics/fight.png")
root.tk.call('wm', 'iconphoto', root._w, img)
# Go to iconarchive website for more icon files

# Second window 
top = tkinter.Toplevel() # Creates another window on top of root. Auto-closes if root closed.
top.title('Second Window')
#Run root window main loop. Must be last line
root.mainloop()
