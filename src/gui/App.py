from gc import collect
from tkinter import PhotoImage
from tkinter import messagebox
import requests
import json
import customtkinter as ctk
from pyexpat.errors import messages

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        ancho = 300
        alto = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (ancho // 2)
        y = (screen_height // 2) - (alto // 2)
        """""//////////////////////////////////// ICONOS //////////////////////////////////////////"""
        self.sunIcon = PhotoImage(file="assets/soleado.png")
        self.titleIcon = PhotoImage(file="assets/WEATHERAPP-removebg-preview (1).png")
        self.waterIcon = PhotoImage(file="assets/agua.png")
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
        self.main()

    def main(self):

        self.headerFrame = ctk.CTkFrame(self, fg_color= "steelblue")
        self.headerFrame.grid(row= 0 , column = 0)
        self.title = ctk.CTkLabel(self.headerFrame, text="",image=self.titleIcon, compound="center",font=("Roboto", 30, "bold")  )
        self.title.grid(row =0 , column = 0 ,padx = 25)
        self.city = ctk.CTkEntry(self.headerFrame, placeholder_text="Elige una ciudad: EJ: Miramar,AR ", width=200)
        self.city.grid(row = 3 , column = 0,pady=10,padx = 50)

#///////////////////////////////////////////////////////////////////////////////////////////////
        self.mainFrame = ctk.CTkFrame(self, fg_color="steelblue")
        self.mainFrame.grid(row = 2 , column = 0)

        self.submitBtn = ctk.CTkButton(self.mainFrame, text="Search" , width=150, command=self.see_temp)
        self.submitBtn.grid( row = 3, column = 1  )
        self.bind("<Return>", lambda event: self.see_temp())


    def see_temp(self):
        self.clear_frame()
        api_key = "928e9266acd34ebd98f142154240911  "
        try :
            ciudad = self.city.get()
            self.city.delete(0, "end")
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

            self.city.destroy()
            self.frameOptions = ctk.CTkFrame(self, width=200, height=50 , fg_color="black")
            self.frameOptions.grid(row = 2 , column = 0,pady=5)
            self.backBtn = ctk.CTkButton(self, text="Back" , width=20, command=self.go_back)
            self.backBtn.grid( row = 3, column = 0, pady=10 )
        except  Exception as ex:
            messagebox.showerror("Error", str(ex))
            self.main()

# ------------------------------------------------------------------------------------------

        self.labelFrame = ctk.CTkFrame(self.frameOptions, fg_color="RoyalBlue4" , corner_radius= 15)
        self.labelFrame.place(row=1,column =0, pady = 20)
        self.labelTemp = ctk.CTkLabel(self.labelFrame, text=str(temp) , image=icono, compound="right", font= ("Impact", 35 , "bold"))
        self.labelTemp.grid(row=0, column=0 ,padx = 10)
        self.tempLabel = ctk.CTkLabel(self.labelFrame,text=estado , font = ("Roboto" , 20 , "bold"))
        self.tempLabel.grid(row = 1, column = 0)
# ------------------------------------------------------------------------------------------

        self.frameWind = ctk.CTkFrame(self.frameOptions, fg_color = "steelblue")
        self.frameWind.grid(row =2 , column =0, pady = 20)
        self.labelWind = ctk.CTkLabel(self.frameWind , text = wind , image = self.vientoNubIcon , compound="right" , font= ("Impact", 35,"bold"))
        self.labelWind.grid( row = 0 , column = 1 ,padx = 10)
#------------------------------------------------------------------------------------------
        self.frameHumity = ctk.CTkFrame(self.frameOptions, fg_color = "steelblue")
        self.frameHumity.grid(row =2 , column =1, pady = 20)
        self.labelHumity = ctk.CTkLabel(self.frameHumity , text = f"{humidity}%" , image = self.waterIcon , compound="right" , font= ("Impact", 35,"bold"))
        self.labelHumity.grid( row = 0 , column = 2 ,padx = 10)



    def clear_frame (self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()

    def clear_frame_options(self):
        for widget in self.frameOptions.winfo_children():
            widget.destroy()

    def go_back(self):
        self.clear_frame_options()
        self.backBtn.destroy()
        self.main()

app = App()
app.mainloop()