#NASA Photo Viewer
import tkinter, requests, webbrowser
from tkcalendar import DateEntry
from PIL import ImageTk, Image
from io import BytesIO
from tkinter import LEFT, filedialog

root = tkinter.Tk()
root.title('NASA Photo Viewer')
#Size of app varies on length of text so geometry and resizable not set
img = tkinter.PhotoImage(file=r"D:\All_Git_Projects\Udemy_Art_of_Doing\App10_NASA_Photo_Viewer\rocket.png")
root.tk.call('wm','iconphoto', root._w, img)

#Define fonts and colors
text_font = ('Times New Roman', 14)
blue_color = '#74BDCB'
lightblue_color = '#04ECF0'
red_color = '#DF362D'
white_color = '#EBF5F7'
root.config(bg=blue_color)

#Define functions
def get_request():
    '''Get request data from NASA APOD API'''
    global response

    # URL and apikey for NASA APOD Viewer request
    url = 'https://api.nasa.gov/planetary/apod'
    apikey = 'tPQeLbYQk3gh78YVUOAUqTqNa4E6c4BWvt3jFfbr'
    date = calendar.get_date()
    querystring = {'date': date, 'api_key':apikey}

    #Call the request and turn it into python usable format
    response = requests.request('GET', url, params=querystring)
    response = response.json()
    set_info()

def set_info():
    '''Set output based on response for api call'''

    # Sample response
    # {'copyright': 'Kristine Richer', 'date': '2021-04-06', 'explanation': "Is this just a lonely tree on an empty hill? To start, 
    # perhaps, but look beyond.  There, a busy universe may wait to be discovered. First, physically, to the left of the tree, is the
    # planet Mars. The red planet, which is the new home to NASA's Perseverance rover, remains visible this month at sunset above the 
    # western horizon. To the tree's right is the Pleiades, a bright cluster of stars dominated by several bright blue stars. The 
    # featured picture is a composite of several separate foreground and background images taken within a few hours of each other, early 
    # last month, from the same location on Vinegar Hill in Milford, Nova Scotia, Canada. At that time, Mars was passing slowly, night 
    # after night, nearly in front of the distant Seven Sisters star cluster. The next time Mars will pass angularly as close to the 
    # Pleiades as it did in March will be in 2038.", 'hdurl': 'https://apod.nasa.gov/apod/image/2104/MartianSisters_Rose_2000.jpg', 
    # 'media_type': 'image', 'service_version': 'v1', 'title': 'Mars and the Pleiades Beyond Vinegar Hill', 
    # 'url': 'https://apod.nasa.gov/apod/image/2104/MartianSisters_Rose_960.jpg'}

    # Update the picture date and explanation
    picture_date.config(text=response['date'])
    picture_explanation.config(text=response['explanation'], justify=LEFT)

    #We need to use 3 images in other functions --> image, thumbnail and full_img
    global img_new
    global thumb
    global full_img

    url = response['url']
    if response['media_type']=='image':
        img_response = requests.get(url, stream=True)

        # Get content of the response and using bytesio for opening the image
        # Keep a reference to the image so as to save it if needed
        # Full screen for the large image in second window
        img_data = img_response.content
        img_new = Image.open(BytesIO(img_data))
        full_img = ImageTk.PhotoImage(img_new)
        thumb_data = img_response.content
        thumb = Image.open(BytesIO(thumb_data))
        thumb.thumbnail((200,200))
        thumb=ImageTk.PhotoImage(thumb)

        #Set thumbnail image
        picture_label.config(image=thumb)
    elif response['media_type']=='video':
        picture_label.config(text=url, image='') #so that previous image is changed to just url
        webbrowser.open(url)

def full_photo():
    '''Open full size photo in new window'''
    top = tkinter.Toplevel()
    top.title('Full Size Photo')
    img_label = tkinter.Label(top,image=full_img)
    img_label.pack()

def save_photo():
    save_name = filedialog.asksaveasfilename(initialdir=r'D:\All_Git_Projects\Udemy_Art_of_Doing\App10_NASA_Photo_Viewer', title='Save Image', filetypes=(("JPEG", "*.jpg"), ("All Files", "*.*")))
    img_new.save(save_name + ".jpg")   

#Define Layout
input_frame = tkinter.Frame(root,bg=lightblue_color)
output_frame = tkinter.Frame(root,bg=white_color)

# Packing the Frames
input_frame.pack()
output_frame.pack(padx=50,pady=(0,25))

#Input Frame widgets
calendar = DateEntry(input_frame, width=10,font=text_font, background=blue_color, foreground=white_color)
submit_button = tkinter.Button(input_frame, text='Submit', font = text_font, bg='#FFA384', command = get_request)
full_button = tkinter.Button(input_frame, text='Full Photo', font = text_font, bg='#FFA384', command=full_photo)
save_button = tkinter.Button(input_frame, text='Save Photo', font = text_font, bg='#FFA384', command=save_photo)
quit_button = tkinter.Button(input_frame, text='Quit', font = text_font, bg=red_color, command = root.destroy)

calendar.grid(row=0, column=0, padx=5, pady=10)
submit_button.grid(row=0, column=1, padx=5, pady=10, ipadx=35)
full_button.grid(row=0, column=2, padx=5, pady=10, ipadx=25)
save_button.grid(row=0, column=3, padx=5, pady=10, ipadx=25)
quit_button.grid(row=0, column=4, padx=5, pady=10, ipadx=50)

#Output frame widgets
picture_date = tkinter.Label(output_frame, font=text_font, bg=white_color)
picture_explanation = tkinter.Label(output_frame, font=text_font, bg=white_color, wraplength=600, anchor='e')
picture_label = tkinter.Label(output_frame)

picture_date.grid(row=1,column=1,padx=10,pady=10)
picture_explanation.grid(row=0,column=0,rowspan=2, padx=10,pady=10)
picture_label.grid(row=0,column=1,padx=10, pady=(10,0))

#Get todays photo on opening the app
get_request()
#Running the mainloop for root window
root.mainloop()