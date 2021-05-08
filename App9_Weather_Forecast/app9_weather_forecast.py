#Weather Forecast App
import tkinter, requests #for api calls
from tkinter import BOTH, IntVar
from PIL import ImageTk,Image
from io import BytesIO #converts the image response to image that can be used

root = tkinter.Tk()
root.title('Weather Forecast')
root.geometry('400x400')
root.resizable(0,0)

img = tkinter.PhotoImage(file=r"D:\All_Git_Projects\Udemy_Art_of_Doing\App9_Weather_Forecast\sun.png")
root.tk.call('wm','iconphoto', root._w, img)


#Define functions
def search():
    '''Use openweather api to look up current weather for a given city or pincode'''
    #Go to openweathermap.org. Register and get api keys in free plan for the api
    global response

    #Get API response
    #URL and the api key for account created in openweather
    url = 'https://api.openweathermap.org/data/2.5/weather'
    apikey = 'XXXXXXXXXXXXXXXXXXX' #add your own key

    #Search by appropriate option selected - city or code
    if selectval.get() == 0:
        querystring = {'q': entry_box.get(), 'appid':apikey, 'units':'imperial'}
    elif selectval.get() == 1:
        querystring = {'zip': entry_box.get(), 'appid':apikey, 'units':'imperial'}
    
    # Call api
    response = requests.request("GET",url,params=querystring) #This gives a status 200 successful response
    response=response.json() #this gets the json dictionary containing the weather info as part of response
    #Sample value in dictionary
    #{'coord': {'lon': 77.2311, 'lat': 28.6128}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 
    # 'icon': '02d'}], 'base': 'stations', 'main': {'temp': 304.76, 'feels_like': 303.53, 'temp_min': 304.54, 'temp_max': 304.76, 
    # 'pressure': 1010, 'humidity': 30, 'sea_level': 1010, 'grnd_level': 986}, 'visibility': 4500, 'wind': {'speed': 1.4, 'deg': 147, 
    # 'gust': 1.31}, 'clouds': {'all': 20}, 'dt': 1620451215, 'sys': {'type': 1, 'id': 9165, 'country': 'IN', 'sunrise': 1620432296, 
    # 'sunset': 1620480612}, 'timezone': 19800, 'id': 1261481, 'name': 'New Delhi', 'cod': 200}
    get_weather()

def get_weather():
    '''get information from api response and update weather labels'''
    city_name = response['name']
    city_lat = str(response['coord']['lat'])
    city_lon = str(response['coord']['lon'])

    main_weather = response['weather'][0]['main']
    description = response['weather'][0]['description']

    temp = str(response['main']['temp'])
    feels_like = str(response['main']['feels_like'])
    temp_min = str(response['main']['temp_min'])
    temp_max = str(response['main']['temp_max'])
    humidity  = str(response['main']['humidity'])
    iconval = response['weather'][0]['icon']

    #update labels
    city_info.config(text = city_name+"("+city_lat+","+city_lon+")", bg = '#E5DDC8', font= ('Arial',12, 'bold') )
    weather_label.config(text=f'Weather: {main_weather}, {description}', font=('Arial',9),bg = '#E5DDC8') #Can use f strings for text
    temp_label.config(text = f'Temperature: {temp} F', font=('Arial',9),bg = '#E5DDC8')
    feels_label.config(text = f'Feels Like: {feels_like} F', font=('Arial',9),bg = '#E5DDC8')
    temp_min_label.config(text = f'Min Temperature: {temp_min} F', font=('Arial',9),bg = '#E5DDC8')
    temp_max_label.config(text = f'Max Temperature: {temp_max} F', font=('Arial',9),bg = '#E5DDC8')
    humidity_label.config(text = f"Humidity: {humidity}", font=('Arial',9),bg = '#E5DDC8')

    # For getting icon image
    global img_icon
    photo_label_url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=iconval)
    icon_response = requests.get(photo_label_url, stream=True)
    img_data = icon_response.content #turn into format tkinter can use
    img_icon = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    photo_label.config(image=img_icon,bg = '#E5DDC8')    

#Define Frames
top_frame = tkinter.Frame(root,bg='#004369')
bottom_frame = tkinter.Frame(root, bg = '#74BDCB')

#Top frame widgets
output_box = tkinter.Frame(top_frame,bg='#E5DDC8', width=40, height=270)
output_box.pack(padx=10,pady=10, fill = BOTH, expand = True)
output_box.pack_propagate(0)

global weather_label_info
#Top frame output box labels
city_info = tkinter.Label(output_box, bg = '#E5DDC8')
weather_label = tkinter.Label(output_box, bg = '#E5DDC8')
temp_label = tkinter.Label(output_box, bg = '#E5DDC8')
feels_label = tkinter.Label(output_box, bg = '#E5DDC8')
temp_min_label = tkinter.Label(output_box, bg = '#E5DDC8')
temp_max_label = tkinter.Label(output_box, bg = '#E5DDC8')
humidity_label = tkinter.Label(output_box, bg = '#E5DDC8')
photo_label = tkinter.Label(output_box, bg = '#E5DDC8')

city_info.pack(pady=8)
weather_label.pack()
temp_label.pack()
feels_label.pack()
temp_min_label.pack()
temp_max_label.pack()
humidity_label.pack()
photo_label.pack(pady=8)

#Bottom frame widgets
selectval = IntVar()
selectval.set(0)
entry_box = tkinter.Entry(bottom_frame, width = 35)
submit_button = tkinter.Button(bottom_frame, bg = '#004369', fg='#FFFFFF', text = 'Submit', command = search)
radio_1 = tkinter.Radiobutton(bottom_frame, text = 'Search by name', bg = '#74BDCB', variable=selectval,value=0)
radio_2 = tkinter.Radiobutton(bottom_frame, text = 'Search by zipcode', bg = '#74BDCB', variable=selectval,value=1) # works with only american 5 digit zipcodes

entry_box.grid(row=0,column=0,padx=10,pady=10, ipady=5)
submit_button.grid(row=0, column=1, padx=10,pady=10,ipady=10, ipadx=30)
radio_1.grid(row=1,column=0,padx=10,pady=10, sticky = 'WE')
radio_2.grid(row=1,column=1,padx=10,pady=10, sticky = 'WE')

# Packing main Frames
top_frame.pack(fill = BOTH, expand = True)
bottom_frame.pack(fill = BOTH, expand = True)

# Running the root window loop
root.mainloop()
