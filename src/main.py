import tkinter as tk
import tkinter.font as tkFont
import json
import requests

from data_model import testing

class Main:
    def __init__(self):
        self.window = tk.Tk()
        self.height = 400
        self.width = 400
        self.title = "JessebotX/WeatherApp"
        self.bg_color = "#121212"
        self.fg_color = "#fff"

        self.h1_font = tkFont.Font(family="Helvetica", size=48)

        self.configure_view()
        self.construct_view()
        self.end_view()

    def configure_view(self):
        self.window.configure(bg="#121212")
        self.window.title(self.title)
        self.window.geometry(str(self.width) + "x" + str(self.height))

    def construct_view(self):
        tk.Label(text = "Weather App", font=self.h1_font, fg="#ffffff", bg="#121212").pack()

    def end_view(self):
        self.window.mainloop()
    

if __name__ == "__main__":
    Main()