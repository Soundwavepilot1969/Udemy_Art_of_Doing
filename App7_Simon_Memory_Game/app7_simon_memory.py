#Simon Memory Game
import tkinter
from tkinter import StringVar, ACTIVE, NORMAL, DISABLED
import random

root=tkinter.Tk()
root.config(bg="#D4F1F4")
root.title("Simon Memory Game")
# root.geometry('300x300')
root.resizable(0,0)

img = tkinter.PhotoImage(file=r"D:\All_Git_Projects\Udemy_Art_of_Doing\App7_Simon_Memory_Game\game.png")
root.tk.call('wm', 'iconphoto', root._w, img)

#Define font and colors
game_font1 = ('Arial', 12)
game_font2 = ('Arial', 8) 
white = "#c6cbcd"
white_light = "#fbfcfc"
magenta = "#90189e"
magenta_light = "#f802f9"
cyan = "#078384"
cyan_light = "#00fafa"
yellow = "#9ba00f"
yellow_light = "#f7f801"
root_color = "#2eb4c6"
game_color = "#f6f7f8"

#Set global variables for the game
time = 500 #tracks speed of game/ sets difficulty
score = 0
game_sequence = []
player_sequence = []

# Define functions
def pick_sequence():
    '''Pick the next value in the sequence, Do not repeat vlaues'''
    while True:
        value = random.randint(1,4)
        #Sequence is size 0 so take the value regardeless
        if len(game_sequence)==0:
            game_sequence.append(value)
            break
        #making sure current value is not the same as last value in sequence
        elif value != game_sequence[-1]:
            game_sequence.append(value)
            break

    # Once all values added play the sequence
    play_sequence()

def play_sequence():
    '''Play the entire sequence for a given round'''
    change_label("Playing")

    #Without delay all buttons animate at the same time. The delay adds time variable to each .after()
    delay=0
    for value in game_sequence:
        if value == 1:
            root.after(delay, lambda:animate(button_1))
        elif value == 2:
            root.after(delay, lambda:animate(button_2))
        elif value == 3:
            root.after(delay, lambda:animate(button_3))
        elif value ==4:
            root.after(delay, lambda:animate(button_4))
        
        #increment delay for next iteration of the loop
        delay+=time

def animate(buttonselect):
    '''Animate a given button by changing its color'''
    buttonselect.config(state=ACTIVE)
    root.after(time, lambda:buttonselect.config(state=NORMAL))

def change_label(message):
    '''Update the new game button to playing and set color for status'''
    new_game.config(text =message)
    if message=='Wrong!':
        new_game.config(bg='red')
    else:
        new_game.config(bg=game_color)

def set_difficulty():
    '''Use radio button to set difficulty and it affects time between time flashes'''
    global time #Change time based on radio button values
    if difficulty.get()=='Easy':
        time = 1000
    elif difficulty.get()=='Medium':
        time = 500
    else:
        time = 200

def pressbutton(buttonval):
    '''simulate button press for player and add value to player sequence'''
    player_sequence.append(buttonval)
    print(player_sequence)

    #If current round is over then check if player sequence and game sequence is the same
    if len(player_sequence)==len(game_sequence):
        check_round()


def check_round():
    '''Determine if player answere correctly'''
    global player_sequence
    global game_sequence
    global score

    if player_sequence==game_sequence:
        change_label('Correct')
        score+=len(player_sequence)+int(1000/time) #more points if difficulty level higher
        root.after(500, pick_sequence) #After will call a function after given time in this case 500ms
    else:
        change_label('Wrong!')
        score=0
        game_sequence=[]
        disable()
        # wait 2 seconds before starting new game
        root.after(2000, lambda:change_label('New Game'))
    player_sequence=[] #wipe player sequence regardless of win or lose
    score_label.config(text="Score :"+str(score)) #update score label to 0

def disable():
    '''Disable buttons when player loses the game'''
    button_1.config(state=DISABLED)
    button_2.config(state=DISABLED)
    button_3.config(state=DISABLED)
    button_4.config(state=DISABLED)

def enable():
    '''Enable all buttons to start game'''
    button_1.config(state=NORMAL)
    button_2.config(state=NORMAL)
    button_3.config(state=NORMAL)
    button_4.config(state=NORMAL)
    pick_sequence()

#Define Frames
top_frame = tkinter.Frame(root, bg="#D4F1F4")
bottom_frame = tkinter.Frame(root, bg="#E9EAEC")

#Defining top frame widgets
new_game = tkinter.Button(top_frame, bg = "#E9EAEC", text = "New Game", font = game_font1, command = enable)
score_label = tkinter.Label(top_frame, bg = "#D4F1F4", text = "Score : "+str(score), font = game_font1)

new_game.grid(row=0,column=0,padx=5,pady=5)
score_label.grid(row=0,column=1)

#Defining bottom frame widgets
button_1 = tkinter.Button(bottom_frame,bg=white, activebackground=white_light,width=15, height = 6, state=DISABLED, command= lambda:pressbutton(1))
button_1.grid(row=0,column=0, columnspan=2, padx=10,pady=10)
button_2 = tkinter.Button(bottom_frame,bg=magenta, activebackground=magenta_light,width=15, height= 6, state=DISABLED, command= lambda:pressbutton(2))
button_2.grid(row=0,column=2, columnspan=2, padx=10,pady=10)
button_3 = tkinter.Button(bottom_frame,bg=cyan, activebackground=cyan_light, width=15, height= 6, state=DISABLED, command= lambda:pressbutton(3))
button_3.grid(row=1,column=0, columnspan=2, padx=10,pady=10)
button_4 = tkinter.Button(bottom_frame,bg=yellow, activebackground=yellow_light, width=15, height= 6, state=DISABLED, command=lambda: pressbutton(4))
button_4.grid(row=1,column=2, columnspan=2, padx=10,pady=10)

difficulty = StringVar() #tracks difficulty of the game
difficulty.set('Medium')
tkinter.Label(bottom_frame, text='Difficulty', font=game_font2,bg=game_color).grid(row=2,column=0)
tkinter.Radiobutton(bottom_frame, text='Easy', variable=difficulty,value='Easy', font = game_font2,bg = game_color, command=set_difficulty).grid(row=2,column=1)
tkinter.Radiobutton(bottom_frame, text='Medium', variable=difficulty,value='Medium', font = game_font2,bg = game_color, command=set_difficulty).grid(row=2,column=2)
tkinter.Radiobutton(bottom_frame, text='Hard', variable=difficulty,value='Hard', font = game_font2,bg = game_color, command=set_difficulty).grid(row=2,column=3)

#Packing Frames
#Packing main frames
top_frame.pack(padx=8,pady=8)
bottom_frame.pack(padx=8,pady=(0,8))
#Running the root window loop
root.mainloop()