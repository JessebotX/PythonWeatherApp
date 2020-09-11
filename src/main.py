import tkinter as tk
import tkinter.font as tkFont
import webbrowser
import imageio

from data import WeatherData

class Main(WeatherData):
    """
    The application's entry point
    """

    def __init__(self):
        """
        The application's constructor
        """
        super().__init__()

        self.window = tk.Tk()
        self.height = 400
        self.width = 400
        self.title = "JessebotX/WeatherApp"
        self.bg_color = "#121212"
        self.fg_color = "#fff"

        self.h1_font = tkFont.Font(family="Helvetica", size=48)
        self.h2_font = tkFont.Font(family="Helvetica", size=36)
        self.h3_font = tkFont.Font(family="Helvetica", size=24)

        self.configure_view()
        self.construct_view()
        self.end_view()

    def configure_view(self):
        """
        Configure the application's window properties
        """
        icon_img = imageio.imread("http://openweathermap.org/img/wn/10d@2x.png")
        imageio.imwrite("weather.ico", icon_img)

        self.window.iconbitmap("weather.ico")
        self.window.configure(bg="#121212")
        self.window.title(self.title)
        self.window.geometry(str(self.width) + "x" + str(self.height))
        self.window.resizable(False, False)

    def construct_view(self):
        """
        Construct the ui elements
        """
        tk.Label(
            text = self.area, 
            font = self.h2_font, 
            fg = self.fg_color, 
            bg = self.bg_color
        ).grid(row=0, column=0)

        # Create line
        tk.Frame(self.window, width=400, height=1, bg=self.fg_color).grid(row=1, column=0)

        # Temperature
        temp_frame = tk.Frame(self.window, bg=self.bg_color)
        temp_frame.grid(row=2, column=0)

        tk.Label(
            temp_frame, 
            text=str(self.fahrenheit) + "°F", 
            bg=self.bg_color, 
            fg="#ffeb3b", 
            font=self.h3_font
        ).grid(row=3, column=3, padx=5)
        tk.Label(
            temp_frame, 
            text=str(self.celsius) + "°C", 
            bg=self.bg_color, 
            fg=self.fg_color, 
            font=self.h3_font
        ).grid(row=3, column=2, padx=5)
        tk.Label(
            temp_frame, 
            text=str(self.kelvin) + "°K", 
            bg=self.bg_color, 
            fg="#f44336", 
            font=self.h3_font
        ).grid(row=3, column=1, padx=5)

        # Create line
        tk.Frame(self.window, width=400, height=1, bg=self.fg_color).grid(row=4, column=0)

        # Weather condition and description
        tk.Label(
            text=self.condition, 
            bg=self.bg_color, 
            fg=self.fg_color, 
            font=self.h2_font
        ).grid(row=5, column=0)
        tk.Label(text=self.description, bg=self.bg_color, fg=self.fg_color).grid(row=6, column=0)

        # Create line
        tk.Frame(self.window, width=200, height=1, bg=self.fg_color).grid(row=7, column=0)

        tk.Label(text="Last updated: " + self.time + "\n from openweathermap.org", bg=self.bg_color, fg=self.fg_color).grid(row=8, column=0)
        tk.Label(
            text="\nCheck out the project on github @", 
            bg=self.bg_color, 
            fg=self.fg_color
        ).grid(row=9, column=0)
        link = tk.Label(
            text="https://github.com/JessebotX/WeatherApp", 
            bg=self.bg_color, 
            fg="#0080ff",
            cursor="hand2"
        )
        link.grid(row=10, column=0)
        link.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/JessebotX/WeatherApp"))

    def end_view(self):
        """
        Complete the loop
        """
        self.window.mainloop()
    

if __name__ == "__main__":
    Main()