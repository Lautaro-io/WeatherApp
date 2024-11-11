import requests
import json
import customtkinter as ctk
from tkinter import PhotoImage
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        ancho = 500
        alto = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (ancho // 2)
        y = (screen_height // 2) - (alto // 2)
#
        """""//////////////////////////////////// ICONOS //////////////////////////////////////////"""
        self.sunIcon = PhotoImage(file="gui/assets/soleado.png")
        self.titleIcon = PhotoImage(file="gui/assets/WEATHERAPP-removebg-preview (1).png")
        self.waterIcon = PhotoImage(file="gui/assets/agua.png")
        self.celsiusIcon = PhotoImage(file="gui/assets/celsius.png")
        self.nightIcon = PhotoImage(file="gui/assets/noche.png")
        self.nightNubIcon = PhotoImage(file="gui/assets/noche-nublada.png")
        self.nubIcon = PhotoImage(file="gui/assets/nublado.png")
        self.vientoNubIcon = PhotoImage(file="gui/assets/viento.png")
        self.sunNubIcon = PhotoImage(file="gui/assets/solnube.png")
        self.stormIcon = PhotoImage(file="gui/assets/strom.png")

        self.resizable(False, False)
        self.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.configure(fg_color="steelblue")
        self.main()

    def main(self):

        self.headerFrame = ctk.CTkFrame(self, fg_color="steelblue")
        self.headerFrame.grid(row=0, column=0,padx = 90)
        self.title = ctk.CTkLabel(self.headerFrame, text="", image=self.titleIcon, compound="center", font=("Roboto", 30, "bold"))
        self.title.grid(row=0, column=0)
        self.city = ctk.CTkEntry(self.headerFrame, placeholder_text_color="gray14",text_color="black",placeholder_text="Elige una ciudad: EJ: Miramar,AR ", width=230,fg_color="white" , border_color="black" , border_width=1)
        self.city.grid(row=3, column=0, pady=10, padx=50 , ipadx=10 ,ipady = 5)

        #///////////////////////////////////////////////////////////////////////////////////////////////
        self.mainFrame = ctk.CTkFrame(self, fg_color="steelblue")
        self.mainFrame.grid(row=2, column=0)
        self.submitBtn = ctk.CTkButton(self.headerFrame, text="Search", width=250, command=self.validar , fg_color="white" , text_color="black" , hover_color="gray"  )
        self.submitBtn.grid(row=4, column=0)
        self.bind("<Return>", lambda event: self.see_temp())
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
    def validar(self):
        city = self.city.get()
        if city :
            self.see_temp()
        else:
            messagebox.showerror("Error", "Error, complete todos los campos.")


    def see_temp(self):
        self.clear_frame()
        self.submitBtn.destroy()
        traducciones_clima = {
            "Clear": "Despejado",
            "Partly cloudy": "Parcialmente nublado",
            "Cloudy": "Nublado",
            "Sunny": "Soleado",
            "Overcast": "Cubierto",
            "Light rain": "Lluvia ligera",
            "Heavy rain": "Lluvia fuerte",
            "Snow": "Nieve",
            "Thunderstorm": "Tormenta"
        }
        api_key = "928e9266acd34ebd98f142154240911"
        ciudad = self.city.get()
        try:

            self.clear_frame()
            self.submitBtn.destroy()
            self.city.delete(0, "end")
            url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={ciudad}"
            response = requests.get(url)

            datos = response.json()
            temp = int(datos["current"]["temp_c"])
            estado = datos["current"]["condition"]["text"]
            estado_es = traducciones_clima.get(estado , estado)
            wind = datos["current"]["wind_kph"]
            humidity = datos["current"]["humidity"]
            registro = f"\nTemperatura actual: {temp}°\nEstado: {estado_es} "
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

            self.city.destroy()
            self.frameOptions = ctk.CTkFrame(self, width=200, height=50, fg_color="steelblue")
            #self.frameOptions.grid_columnconfigure((0, 1, 2), weight=1)
            self.frameOptions.grid(row=1, column=0, pady=15,padx=10)

            self.backBtn = ctk.CTkButton(self, text="Back", width=200, command=self.go_back , fg_color="white", hover_color="gray" , text_color="black")
            self.backBtn.grid(row=2, column=0, pady=10)

            # ------------------------------------------------------------------------------------------
            self.center = ctk.CTkFrame(self.frameOptions, fg_color="steelblue" )
            self.center.grid(row=0, column=1, sticky="nsew",pady = 5)

            self.labelFrame = ctk.CTkFrame(self.center, fg_color="steelblue", corner_radius=20)
            self.labelFrame.grid(row=0, column=0, sticky="nsew",ipady= 10 ,ipadx = 10,pady = 5,padx = 120)
            self.labelTemp = ctk.CTkLabel(self.labelFrame, text="", image=icono, compound="center", font=("Impact", 35, "bold"))
            self.labelTemp.grid(row=0, column=1, sticky = "nsew",padx = 50)
            self.tempLabel = ctk.CTkLabel(self.labelFrame, text=registro, font=("Roboto", 20, "bold"))
            self.tempLabel.grid(row=1, column=1, sticky = "nsew")

            # ------------------------------------------------------------------------------------------

            self.frameWind = ctk.CTkFrame(self.center, fg_color="steelblue")
            self.frameWind.grid(row=2, column=0, pady=10, sticky="nsew")
            self.labelWind = ctk.CTkLabel(self.frameWind, text=f"{wind}\nKm/h", image=self.vientoNubIcon, compound="right", font=("Impact", 35, "bold"))
            self.labelWind.grid(row=0, column=0, padx=10, sticky = "nsew",ipady = 5)
##
            # ------------------------------------------------------------------------------------------
            self.frameHumity = ctk.CTkFrame(self.center, fg_color="steelblue")
            self.frameHumity.grid(row=2, column=0, pady=10, sticky="nsew", padx=350)
            self.labelHumity = ctk.CTkLabel(self.frameHumity, text=f"{humidity}%", image=self.waterIcon, compound="right", font=("Impact", 35, "bold"))
            self.labelHumity.grid(row=0, column=0, sticky = "nsew")
        except Exception as ex:
            messagebox.showerror("",str(ex))

    def clear_frame(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()

    def clear_frame_options(self):
        for widget in self.frameOptions.winfo_children():
            widget.destroy()

    def go_back(self):
        self.clear_frame_options()
        self.backBtn.destroy()
        self.main()


