#Morse Code Translator
import tkinter
from tkinter import IntVar, END, DISABLED, NORMAL
from PIL import ImageTk, Image
from playsound import playsound #install these using pip install if not present in pc

root=tkinter.Tk()
root.config(bg="#D4F1F4")
root.title("Morse Code Translator")
# root.geometry('500x350')
root.resizable(0,0)

img = tkinter.PhotoImage(file=r"D:\All_Git_Projects\Udemy_Art_of_Doing\App6_Morse_Code_Translator\code.png")
root.tk.call('wm', 'iconphoto', root._w, img)

#Define colors and fonts
button_color = '#05445E'
button_font = ('Simsun',10)

#Define functions
def delete_text():
    input_text.delete(1.0,END)
    output_text.delete(1.0,END)

def convert_lang():
    '''Call the appropriate conversion based on radio button selection'''
    if language.get()==1:
        convert_to_morse()
    elif language.get()==2:
        convert_to_english()

def convert_to_morse():
    '''Convert english message to morse'''
    morse_code = "" #Stores the morse code

    #Convert english text to lower case
    english_text = input_text.get('1.0',END)
    english_text=english_text.lower()

    # Iterate through text and replace chars not in dictionary with ''
    for letter in english_text:
        if letter not in english_morse:
            english_text=english_text.replace(letter,'')
    
    #Break up text into words and store in list
    word_list = english_text.split(' ')
    
    #Turn each individual word in word_list into list of letters
    for word in word_list:
        letters=list(word)
        #For each letter get morse code and append to morse_code
        for letter in letters:
            morse_char = english_morse[letter]
            morse_code+=morse_char
            morse_code+=" "
        #Separate individual words with a |
        morse_code+='|'

    output_text.insert("1.0",morse_code)


def convert_to_english():
    '''Convert Morse Code Message to English'''
    english="" #To store english

    #get text
    morse_text = input_text.get('1.0',END)
    
    # Iterate through text and replace chars not in morse code dictionary with ''
    for letter in morse_text:
        if letter not in morse_english.keys():
            morse_text=morse_text.replace(letter,'')

    #Break up each word based on |
    word_list = morse_text.split('|')
    
    #Turn each individual word in word_list into list of letters
    for word in word_list:
        letters=word.split(" ")
        
        #For each letter get english char and append to string english 
        for letter in letters:
            english_char = morse_english[letter]
            english+=english_char
            
        #Separate individual words with a space ' '
        english+=' '

    output_text.insert("1.0",english)

def play():
    '''Play the morse code for morse text'''
    if language.get()==1:
        text=output_text.get(1.0,END)
    elif language.get()==2:
        text=input_text.get(1.0,END)
    
    #Play the tones
    for value in text:
        if value == ".":
            playsound(r'D:\All_Git_Projects\Udemy_Art_of_Doing\App6_Morse_Code_Translator\dot.mp3')
            root.after(75) #stopping the looping of the root window so that sound is not continuous
        elif value == "-":
            playsound(r'D:\All_Git_Projects\Udemy_Art_of_Doing\App6_Morse_Code_Translator\dash.mp3')
            root.after(150)
        elif value == ' ':
            root.after(225)
        elif value == '|':
            root.after(525)

def show_guide():
    '''Show morse code guide in new window'''
    #Morse needs to be a global variable to put on our window
    #window guide needs to be global to close in another function
    global morse
    global guide

    #Create second window
    guide = tkinter.Toplevel()
    guide.title("Morse Guide")
    guide.geometry('350x350+'+str(root.winfo_x()+500)+"+"+str(root.winfo_y()))
    guide.config(bg="#D4F1F4")

    #Create image label and pack it
    morse = ImageTk.PhotoImage(Image.open(r'D:\All_Git_Projects\Udemy_Art_of_Doing\App6_Morse_Code_Translator\morse_chart.jpg')) #jpg wont work with just tkinter needs PIL imagetk
    label = tkinter.Label(guide,image=morse,bg="#189AB4")
    label.pack(padx=10,pady=5,ipadx=5,ipady=5)

    #Disable guide button
    guide_button.config(state=DISABLED)

    #create close button
    close_guide = tkinter.Button(guide, bg=button_color, font = button_font,text='Close Guide',fg="#FFFFFF", command=hide_guide)
    close_guide.pack(padx=10,pady=(0,5),ipadx=20,ipady=5)

def hide_guide():
    '''Closes the guide window'''
    guide.destroy()
    guide_button.config(state=NORMAL)

#Define dictionaries for morse code
english_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 
'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..--', 'v': '...-', 'w': '.--', 'x': '-..-',
'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
'6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ':' ', '|':'|', "":"" }

morse_english = dict([(value, key) for key, value in english_morse.items()]) #reversing the above dictionary flipping keys and values

# Define Frames
top_frame = tkinter.LabelFrame(root, bg='#189AB4')
bottom_frame = tkinter.LabelFrame(root,bg='#189AB4')

#Define widgets for top_frame
input_text = tkinter.Text(top_frame, height = 8, width = 30, bg = "#D4F1F4")
input_text.grid(row=0,column=1,rowspan=3,padx=5,pady=5)

#Variable to track radio button
language = IntVar()
language.set(1)

english_morse_radio = tkinter.Radiobutton(top_frame, text='English --> Morse Code', bg='#189AB4', variable=language,value=1,font=button_font)
morse_english_radio = tkinter.Radiobutton(top_frame, text='Morse Code --> English', bg='#189AB4', variable=language,value=2,font=button_font)
guide_button = tkinter.Button(top_frame, bg=button_color, text='Guide',fg='#FFFFFF', command = show_guide)
english_morse_radio.grid(row=0,column=0,padx=5,pady=5)
morse_english_radio.grid(row=1,column=0,padx=5,pady=(0,5))
guide_button.grid(row=2,column=0,padx=5,sticky='WE',ipadx=40)

# Define widgets for bottom frame
output_text = tkinter.Text(bottom_frame, height = 8, width = 30, bg = "#D4F1F4")
output_text.grid(row=0,column=1,rowspan=4,padx=5,pady=5)
convert_button = tkinter.Button(bottom_frame, bg=button_color, text='Convert',fg='#FFFFFF', command = convert_lang)
convert_button.grid(row=0,column=0,padx=5,pady=5,ipadx=65,sticky='WE')
playmorse_button = tkinter.Button(bottom_frame, bg=button_color, text='Play Morse',fg='#FFFFFF', command=play)
playmorse_button.grid(row=1,column=0,padx=5,pady=5,sticky='WE')
clear_button = tkinter.Button(bottom_frame, bg=button_color, text='Clear',fg='#FFFFFF', command=delete_text)
clear_button.grid(row=2,column=0,padx=5,pady=5,sticky='WE')
quit_button = tkinter.Button(bottom_frame, bg=button_color, text='Quit',fg='#FFFFFF', command = root.destroy)
quit_button.grid(row=3,column=0,padx=5,pady=5,sticky='WE')

#Packing main frames
top_frame.pack(padx=8,pady=8)
bottom_frame.pack(padx=8,pady=(0,8))

#Running the root window loop
root.mainloop()