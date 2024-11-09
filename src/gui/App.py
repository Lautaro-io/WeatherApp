from gc import collect
from tkinter import PhotoImage

import requests
import json
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        ancho = 350
        alto = 450
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (ancho // 2)
        y = (screen_height // 2) - (alto // 2)
        """""//////////////////////////////////// ICONOS //////////////////////////////////////////"""
        self.sunIcon = PhotoImage(file="assets/soleado.png")

        self.waterIcon = PhotoImage(file="assets/soleado.png")
        self.celsiusIcon = PhotoImage(file="assets/celsius.png")
        self.nightIcon = PhotoImage(file="assets/noche.png")
        self.nightNubIcon = PhotoImage(file="assets/noche-nublada.png")
        self.nubIcon = PhotoImage(file="assets/nublado.png")
        self.vientoNubIcon = PhotoImage(file="assets/viento.png")
        self.sunNubIcon = PhotoImage(file="assets/solnube.png")
        self.stormIcon = PhotoImage(file="assets/strom.png")



        self.resizable(False,False)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.configure(fg_color="steelblue")

        self.headerFrame = ctk.CTkFrame(self, fg_color= "steelblue", height= 10)
        self.headerFrame.grid(row= 0 , column = 0)
        self.title = ctk.CTkLabel(self.headerFrame, text="""WeatherApp""", font=("Roboto", 30, "bold"))
        self.title.grid(row =0 , column = 0, pady = 10 )
        self.sun = ctk.CTkLabel(self.headerFrame,text = "",image=self.sunIcon)
        self.sun.grid(row = 1 , column= 0  )
#///////////////////////////////////////////////////////////////////////////////////////////////
        self.mainFrame = ctk.CTkFrame(self, fg_color="steelblue")
        self.mainFrame.grid(row = 2 , column = 0)
        self.grid_columnconfigure(0 , weight= 1)
        self.grid_columnconfigure(1 , weight= 1)
        self.grid_columnconfigure(2 , weight= 1)
        self.city = ctk.CTkEntry(self.headerFrame, placeholder_text="Elige una ciudad: EJ: Miramar,AR ", width=200)
        self.city.grid(row = 3 , column = 0,pady=10,padx = 75)
        self.submitBtn = ctk.CTkButton(self.mainFrame, text="See weather", command=self.see_temp)
        self.submitBtn.grid( row = 5, column = 0 , pady=10 , padx = 75)

    def see_temp(self):
        self.clear_frame()
        api_key = "928e9266acd34ebd98f142154240911  "
        ciudad = self.city.get()
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={ciudad}"
        response = requests.get(url)

        datos = response.json()
        temp = int(datos["current"]["temp_c"])
        estado = datos["current"]["condition"]["text"]
        wind = datos["current"]["wind_kph"]
        humidity = datos["current"]["humidity"]
        registro = f"\nTemperatura Actual:{temp}grados Celsius\nViento: {wind} km/h\nHumedad : {humidity}% "
        if estado == "Sunny":
            icono = self.sunIcon
        elif estado == "Partly cloudy":
            icono = self.sunNubIcon
        elif estado == "Cloudy":
            self.configure(fg_color="gray52")
            icono = self.nubIcon
        elif estado == "Rain":
            self.configure(fg_color="gray52")
            icono = self.waterIcon
        elif estado == "Thunderstorm":
            self.configure(fg_color="gray52")

            icono = self.stormIcon
        else:
            icono = self.celsiusIcon
        registro = f"Temperatura: {temp}°C\nViento: {wind} km/h\nHumedad: {humidity}%"
        self.frameOptions = ctk.CTkFrame(self.mainFrame, width=200, height=50 , fg_color="steelblue")
        self.frameOptions.grid(row = 4 , column = 0,pady=5)
        self.submitBtn = ctk.CTkButton(self.mainFrame, text="See weather", command=self.see_temp)
        self.submitBtn.grid( row = 5, column = 0 , pady=10 , padx = 75)

        self.labelTemp = ctk.CTkLabel(self.frameOptions, text=str(temp) , image=icono, compound="right", font= ("Impact", 35 , "bold"))
        self.labelTemp.grid(row=1, column=0, pady=10)

        self.frameWind = ctk.CTkFrame(self.frameOptions, fg_color = "steelblue")
        self.frameWind.grid(row =1 , column =0)

        self.labelWind = ctk.CTkLabel(self.frameWind , text = wind , image = self.vientoNubIcon , compound="right" , font= ("Impact", 20,"bold"))
        self.labelWind.grid( row = 0 , column = 1)

        self.frameHumity = ctk.CTkFrame(self.frameOptions, fg_color = "steelblue")
        self.frameHumity.grid(row =1 , column =2)

        self.frameHumity = ctk.CTkLabel(self.frameHumity , text = f"{humidity}%" , image = self.waterIcon , compound="right" , font= ("Impact", 20,"bold"))
        self.frameHumity.grid( row = 0 , column = 0)




    def clear_frame (self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()
app = App()
app.mainloop()