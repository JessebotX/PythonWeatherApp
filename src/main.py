import tkinter as tk
import tkinter.font as tkFont
import webbrowser
import imageio
import os

from data import WeatherData

class Main(WeatherData):
    """
    The application's entry point
    """

    def __init__(self):
        """
        The application's constructor
        """
        self.window = tk.Tk()
        self.height = 400
        self.width = 400
        self.title = "JessebotX/WeatherApp"
        self.bg_color = "#121212"
        self.fg_color = "#fff"

        self.cityEntry = ""
        self.countryEntry = ""

        self.h1_font = tkFont.Font(family="Helvetica", size=48)
        self.h2_font = tkFont.Font(family="Helvetica", size=36)
        self.h3_font = tkFont.Font(family="Helvetica", size=24)

        self.setState()

    def setState(self, city="Vancouver", country="CA", first_time = True):
        self.begin(city + "," + country)

        if not first_time:
            self.forget_view()

        self.configure_view()
        self.construct_view()
        self.end_view()

    def configure_view(self):
        """
        Configure the application's window properties
        """
        # if os.path.isfile("weather.ico"):
        #     os.remove("weather.ico")
        
        # icon_img = imageio.imread("http://openweathermap.org/img/wn/" + self.icon_id + "@2x.png")
        # imageio.imwrite("weather.ico", icon_img)

        self.window.iconbitmap("weather.ico")
        self.window.configure(bg="#121212")
        self.window.title(self.title)
        self.window.geometry(str(self.width) + "x" + str(self.height))
        self.window.resizable(False, False)

    def construct_view(self):
        """
        Construct the ui elements
        """
        self.displayAreaLabel = tk.Label(
            text = self.area, 
            font = self.h2_font, 
            fg = self.fg_color, 
            bg = self.bg_color
        )
        self.displayAreaLabel.grid(row=0, column=0)

        # Create line
        self.horizontalLine1 = tk.Frame(self.window, width=400, height=1, bg=self.fg_color)
        self.horizontalLine1.grid(row=1, column=0)

        # Temperature
        self.temp_frame = tk.Frame(self.window, bg=self.bg_color)
        self.temp_frame.grid(row=2, column=0)

        self.displayFahrenheitLabel = tk.Label(
            self.temp_frame, 
            text=str(self.fahrenheit) + "°F", 
            bg=self.bg_color, 
            fg="#ffeb3b", 
            font=self.h3_font
        )
        self.displayFahrenheitLabel.grid(row=3, column=3, padx=5)
        self.displayCelsiusLabel = tk.Label(
            self.temp_frame, 
            text=str(self.celsius) + "°C", 
            bg=self.bg_color, 
            fg=self.fg_color, 
            font=self.h3_font
        )
        self.displayCelsiusLabel.grid(row=3, column=2, padx=5)
        self.displayKelvinLabel = tk.Label(
            self.temp_frame, 
            text=str(self.kelvin) + "°K", 
            bg=self.bg_color, 
            fg="#f44336", 
            font=self.h3_font
        )
        self.displayKelvinLabel.grid(row=3, column=1, padx=5)

        # Create line
        self.horizontalLine2 = tk.Frame(self.window, width=400, height=1, bg=self.fg_color)
        self.horizontalLine2.grid(row=4, column=0)

        # Weather condition and description
        self.displayConditionLabel = tk.Label(
            text=self.condition, 
            bg=self.bg_color, 
            fg=self.fg_color, 
            font=self.h2_font
        )
        self.displayConditionLabel.grid(row=5, column=0)
        self.displayDescriptionLabel = tk.Label(text=self.description, bg=self.bg_color, fg=self.fg_color)
        self.displayDescriptionLabel.grid(row=6, column=0)

        # Create line
        self.horizontalLine3 = tk.Frame(self.window, width=200, height=1, bg=self.fg_color)
        self.horizontalLine3.grid(row=7, column=0)

        self.displayTimeLabel = tk.Label(
            text="Last updated: " + self.time + "\n from openweathermap.org", 
            bg=self.bg_color, 
            fg=self.fg_color
        )
        self.displayTimeLabel.grid(row=8, column=0)
        self.displaySeeAlsoLabel = tk.Label(
            text="\nCheck out the project on github @", 
            bg=self.bg_color, 
            fg=self.fg_color
        )
        self.displaySeeAlsoLabel.grid(row=9, column=0)
        self.link = tk.Label(
            text="https://github.com/JessebotX/WeatherApp", 
            bg=self.bg_color, 
            fg="#0080ff",
            cursor="hand2"
        )
        self.link.grid(row=10, column=0)
        self.link.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/JessebotX/WeatherApp"))

        # Create line
        self.horizontalLine4 = tk.Frame(self.window, width=200, height=1, bg=self.fg_color)
        self.horizontalLine4.grid(row=11, column=0)

        self.enterFrame = tk.Frame(self.window, bg=self.bg_color)
        self.enterFrame.grid(row=12, pady=5)
        self.displayCityLabel = tk.Label(self.enterFrame, text="Enter city", bg=self.bg_color, fg=self.fg_color)
        self.displayCityLabel.grid(row=1, column=1)
        self.cityEntry = tk.Entry(self.enterFrame)
        self.cityEntry.grid(row=1, column=2)
        self.countryLabel = tk.Label(
            self.enterFrame, 
            text="(OPTIONAL) Enter [ISO-3166] Country Code \n(i.e \"US\" = United States of America)",
            bg=self.bg_color,
            fg="#0080ff",
            cursor="hand2"
        )
        self.countryLabel.grid(row=2, column=1)
        self.countryLabel.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.iso.org/obp/ui/#search"))
        self.countryEntry = tk.Entry(self.enterFrame)
        self.countryEntry.grid(row=2, column=2)
        self.displaySubmitButton = tk.Button(self.enterFrame, text="Enter", command=self.submit)
        self.displaySubmitButton.grid(row=3)

    def submit(self):
        self.setState(city=self.cityEntry.get(), country=self.countryEntry.get(), first_time=False)

    def end_view(self):
        """
        Complete the loop
        """
        self.window.mainloop()

    def forget_view(self):
        self.displayAreaLabel.grid_forget()
        self.temp_frame.grid_forget()
        self.displayConditionLabel.grid_forget()
        self.displayDescriptionLabel.grid_forget()

if __name__ == "__main__":
    Main()
