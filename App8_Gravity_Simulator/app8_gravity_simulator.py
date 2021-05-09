#Gravity Simulator
import tkinter, matplotlib
from tkinter import BOTH,HORIZONTAL,CURRENT, END
from matplotlib import pyplot

root=tkinter.Tk()
root.config(bg="#D4F1F4")
root.title("Gravity Sim")
# root.geometry('600x650')
root.resizable(0,0)

img = tkinter.PhotoImage(file=r"D:\All_Git_Projects\Udemy_Art_of_Doing\App8_Gravity_Simulator\earth.png")
root.tk.call('wm', 'iconphoto', root._w, img)

#Define global variables
time = 0
data = {}
for i in range(1,5):
    data[f'data_{i}'] = [] #Blank list to which values will be appended when step function is run

# Define functions

def move(event):
    '''Drag the balls vertically and set position'''
    #Move only if current object selected is the ball using tags
    if 'BALL' in main_canvas.gettags(CURRENT):
        #Record x position of ball and fix it
        x1 = main_canvas.coords(CURRENT)[0] #Current gives coordinates of object on canvas where the mouse is clicking
        x2 = main_canvas.coords(CURRENT)[2]

        #Change the coords of CURRENT object based on the even.y position of the mouse.
        main_canvas.coords(CURRENT,x1,event.y,x2,event.y+10)
        
        #Making ball not able to move beyond canvas
        if main_canvas.coords(CURRENT)[3] < 15:
            main_canvas.coords(CURRENT,x1,5,x2,15)
        elif main_canvas.coords(CURRENT)[3] > 415:
            main_canvas.coords(CURRENT,x1,405,x2,415)
    
    #update height for the ball in the dictionary
    update_height()

def update_height():
    '''Update the height of the ball on moving it'''
    for i in range(1,5):
        heights[f'height_{i}'].config(text='Height: '+str(round(415-main_canvas.coords(balls[f'ball{i}'])[3],2)))
         
def step(t): #t is value on slider passed through lambda function
    '''Move ball one step based on the time slider value of t'''
    global time
    #loop through all 4 balls
    for i in range(1,5):
        #Negate a and v as canvas y and x values increase as you move down in the canvas
        a = -1*float(accelerations[f'a_{i}'].get())
        v = -1*float(velocities[f'v_{i}'].get())
        d = v*t+0.5*a*t**2 #distance = ut+1/2at^2
        #Get x coords for current ball that remains constant
        x1 = main_canvas.coords(balls[f'ball{i}'])[0]
        x2 = main_canvas.coords(balls[f'ball{i}'])[2]

        #move the  ball and create a dash line to mark the new position
        if main_canvas.coords(balls[f'ball{i}'])[3]+d <=415:
            main_canvas.move(balls[f'ball{i}'],0,d)
            y2 = main_canvas.coords(balls[f'ball{i}'])[3]
            main_canvas.create_line(x1,y2,x2,y2,tag='DASH') #Setting line to DASH helps with removing it later
        else:
            main_canvas.coords(balls[f'ball{i}'], x1, 405, x2, 415)

        vf = v+a*t#Update velocity values for each ball
        velocities[f'v_{i}'].delete(0,END)
        velocities[f'v_{i}'].insert(0,str(round(-1*vf, 2)))

        #Add values to the data dictionary set with empty list
        data[f'data_{i}'].append((time, 415-main_canvas.coords(balls[f'ball{i}'])[3]))

        #Update heights for the given time interval
        update_height()

        #update time
        time+=t

def run():
    '''run the entire simulation until balls beyond screen or on the ground'''
    # Balls can be on the ground or on moved up on the screen so we need to call step atleast Once
    step(t_slider.get())
    # Run step until balls reach their conclusion - ground or off screen
    # While loop keeps going as long as there is one ball on the screen
    while 15 < main_canvas.coords(balls['ball1'])[3] < 415 or 15 < main_canvas.coords(balls['ball2'])[3] < 415 or 15 < main_canvas.coords(balls['ball3'])[3] < 415 or 15 <main_canvas.coords(balls['ball4'])[3] < 415:
        step(t_slider.get())

def graph():
    '''Graph distance v time for 4 balls'''
    #Colors of the balls corresponds to colors of the graph
    colors = ['red', 'green', 'blue', 'yellow']
    for i in range(1,5):
        #initialize x,y values
        x=[]
        y=[]
        #Add corresponding data to x,y values
        for data_list in data[f'data_{i}']:
            x.append(data_list[0])
            y.append(data_list[1])
        #Plot data in corresponding color
        pyplot.plot(x,y,color=colors[i-1])
    #Formatting graph
    pyplot.title('Distance VS Time Graph')
    pyplot.xlabel('Time')
    pyplot.ylabel('Distance')
    pyplot.show()


def reset():
    '''Erase all "DASH" tags from canvas, set balls back to ground, and reset entry fields.'''
    global time
    time = 0
    main_canvas.delete("DASH") #Deletes objects on canvas with tag DASH
    #Clear each ball...
    for i in range(1,5):
        # Clear and set the velocity and accelerations
        velocities[f'v_{i}'].delete(0, END)
        velocities[f'v_{i}'].insert(0, '0')
        accelerations[f'a_{i}'].delete(0, END)
        accelerations[f'a_{i}'].insert(0, '0')
        # Reset ball to starting position
        main_canvas.coords(balls[f'ball{i}'], 45+(i-1)*100, 405, 55+(i-1)*100, 415)
        # Clear data
        data[f'data_{i}'].clear()
    update_height()
    t_slider.set(1)

# Define frames
canvas_frame = tkinter.Frame(root)
input_frame = tkinter.Frame(root)
canvas_frame.pack(pady=5)
input_frame.pack(fill = BOTH, expand=True)

canvas_frame.pack_propagate(0)
input_frame.pack_propagate(0)

#Define widgets
main_canvas = tkinter.Canvas(canvas_frame, width=400, height=415,bg='white')
main_canvas.grid(row=0,column=0,padx=5,pady=5)

line_0 = main_canvas.create_line(2,0,2,415) #2 used instead of 0 because line will not be seen on canvas. x1,y1 and x2,y2 coordinates
line_1 = main_canvas.create_line(100,0,100,415)
line_2 = main_canvas.create_line(200,0,200,415)
line_3 = main_canvas.create_line(300,0,300,415)
line_4 = main_canvas.create_line(400,0,400,415)

balls = {} #dictionary for the balls
balls['ball1'] = main_canvas.create_oval(45,405,55,415,fill='red',tag='BALL') #Added BALL tag so that only object with that tag can be moved
balls['ball2'] = main_canvas.create_oval(145,405,155,415,fill='green',tag='BALL')
balls['ball3'] = main_canvas.create_oval(245,405,255,415,fill='blue',tag='BALL')
balls['ball4'] = main_canvas.create_oval(345,405,355,415,fill='yellow',tag='BALL')

#Input frame 
tkinter.Label(input_frame,text='d').grid(row=0,column=0, ipadx=10)
tkinter.Label(input_frame,text='vi').grid(row=1,column=0)
tkinter.Label(input_frame,text='a').grid(row=2,column=0)
tkinter.Label(input_frame,text='t').grid(row=3,column=0)

#Dictionary for heights label that captures height of the ball on the canvas
heights = {}
for i in range(1,5):
    heights[f'height_{i}']=tkinter.Label(input_frame,text='Height: '+str(415-main_canvas.coords(balls[f'ball{i}'])[3]))
    heights[f'height_{i}'].grid(row=0,column=i)

# Velocity entry boxes
velocities = {}
for i in range(1,5):
    velocities[f'v_{i}']=tkinter.Entry(input_frame, width=14)
    velocities[f'v_{i}'].grid(row=1,column=i,padx=1)
    velocities[f'v_{i}'].insert(0,'0')

#Acceleration entry boxes
accelerations = {}
for i in range(1,5):
    accelerations[f'a_{i}']=tkinter.Entry(input_frame, width=14)
    accelerations[f'a_{i}'].grid(row=2,column=i,padx=1)
    accelerations[f'a_{i}'].insert(0,'0')

#Time slider
t_slider = tkinter.Scale(input_frame, from_=0,to=1, tickinterval=.1,resolution=.01,orient=HORIZONTAL)
t_slider.grid(row=3,column=1,columnspan=4,sticky='WE')
t_slider.set(1)

# buttons
step_button=tkinter.Button(input_frame,text='Step', command=lambda:step(t_slider.get()))
run_button=tkinter.Button(input_frame,text='Run',command=run)
graph_button=tkinter.Button(input_frame,text='Graph',command=graph)
reset_button=tkinter.Button(input_frame,text='Reset',command=reset)
quit_button=tkinter.Button(input_frame,text='Quit', command=root.destroy)

step_button.grid(row=4,column=1,pady=(10,0),sticky='WE')
run_button.grid(row=4,column=2,pady=(10,0),sticky='WE')
graph_button.grid(row=4,column=3,pady=(10,0),sticky='WE')
reset_button.grid(row=4,column=4,pady=(10,0),sticky='WE')
quit_button.grid(row=5,column=1,columnspan=4,pady=(0,10),sticky='WE')

#Making each ball dragable in the vertical direction
# Binding left click to specific function. Here its button press to function move
root.bind('<B1-Motion>',move)

#Running main root loop
root.mainloop()