import requests, json
from tkinter import *


def fetch():

    api_key = "8ec6af652686cbe5b7b800002c8fba1a"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = i.get()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)


    x = response.json()
    if x["cod"] != "404":


        y = x["main"]


        '''current_temperature = y["temp"]
        current_temperature= int(current_temperature)
        current_temperature=current_temperature - 273
        temp = current_temperature'''


        temp = int(y['temp']) - 273
        current_pressure = y["pressure"]

        '''current_humidity = y["humidity"]
        current_humidity = float(current_humidity)
        current_humidity= current_humidity/100'''

        humid = float(y['humidity']) / 100
        z = x["weather"]

        weather_description = z[0]["description"]
        label1.config(text=str(temp) + ' C')
        label2.config(text=str(current_pressure) + ' hPa')
        label3.config(text=str(humid))
        label4.config(text=str(weather_description))

        result = (" Temperature= " +
                  str(temp) + " C" +
                  "\n atmospheric pressure = " +
                  str(current_pressure) + " hPa" +
                  "\n humidity = " +
                  str(humid) +
                  "\n description = " +
                  str(weather_description))
        print(result)

    else:
        print(" City Not Found ")


root = Tk()
root.title('Weather Forecast')
root.configure(bg='light blue')
root.resizable(800,800)
w = Label(root, text='Enter the name of the city to fetch the weather:')
w.config(bg="purple", fg="black")
i = Entry(root)

b = Button(root, text='Submit', command=fetch, bg='cyan4')
l1 = Label(root, text='Temperature :')
label1 = Label(root, text='')
l1.config(bg="purple", fg="black")
l2 = Label(root, text='Pressure :')
label2 = Label(root, text='')
l2.config(bg="purple", fg="black")
l3 = Label(root, text='Humidity :')
label3 = Label(root, text='')
l3.config(bg="purple", fg="black")
l4 = Label(root, text='Weather :')
label4 = Label(root, text='')
l4.config(bg="purple", fg="black")
w.pack()
i.pack()
b.pack()
l1.pack()
label1.pack()
l2.pack()
label2.pack()
l3.pack()
label3.pack()
l4.pack()
label4.pack()
root.mainloop()
