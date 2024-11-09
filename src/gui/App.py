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
        sunIcon = PhotoImage(file="src/assets/soleado.png")
        # waterIcon = PhotoImage(file="src/assets/soleado.png")
        # celsiusIcon = PhotoImage(file="src/assets/soleado.png")
        # nightIcon = PhotoImage(file="src/assets/soleado.png")
        # nightNubIcon = PhotoImage(file="src/assets/soleado.png")
        # nubIcon = PhotoImage(file="src/assets/soleado.png")
        # vientoNubIcon = PhotoImage(file="src/assets/soleado.png")
        # nubIcon = PhotoImage(file="src/assets/soleado.png")
        # stormIcon = PhotoImage(file="src/assets/soleado.png")




        self.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.configure(fg_color="steelblue")
        self.title = ctk.CTkLabel(self, text="""WeatherApp
        beta""", font=("Roboto", 30, "bold"))
        self.resizable(False,False)
        self.title.grid(row =0 , column = 0, pady=10)
        self.grid_columnconfigure(0 , weight= 1)
        self.grid_columnconfigure(2 , weight= 1)
        self.grid_columnconfigure(3 , weight= 1)
        self.city = ctk.CTkEntry(self, placeholder_text="Elige una ciudad: EJ: Miramar,AR ", width=200)
        self.city.grid(row = 2 , column = 0,pady=10,padx = 75)
        self.frameOptions = ctk.CTkFrame(self, width=200, height=50)
        self.frameOptions.grid(row = 3 , column = 0,pady=5)
        self.labelTemp = ctk.CTkLabel(self.frameOptions, text="")
        self.labelTemp.grid(row = 0 , column = 0, pady=10)
        self.submitBtn = ctk.CTkButton(self, text="See weather", command=self.see_temp)
        self.submitBtn.grid( row = 4, column = 0 , pady=10 , padx = 75)

    def see_temp(self):
        api_key = "928e9266acd34ebd98f142154240911  "
        ciudad = self.city.get()
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={ciudad}"
        response = requests.get(url)

        datos = response.json()
        ciudad = datos["location"]["name"]
        pais = datos["location"]["country"]
        temp = datos["current"]["temp_c"]
        wind = datos["current"]["wind_kph"]
        humidity = datos["current"]["humidity"]
        registro = f"City : {ciudad}\nPais: {pais}\nTemperatura Actual:{temp}grados Celsius\nViento: {wind} km/h\nHumedad : {humidity}% "
        print(registro)
        self.labelTemp.configure(text=registro)


app = App()
app.mainloop()