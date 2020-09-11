import json
import requests
import os

from data_model import DataModel

class WeatherData(DataModel):
    def __init__(self):
        super().__init__()
        self.current = None
        self.currentReq = None

        # set apikey to the read file
        with open("src/private.json", "r") as config:
            self.apikey = json.loads(config.read())

        self.connect_api()
        self.set_data()
    
    def connect_api(self):
        """
        Connect to openweathermap's api
        """
        try: 
            self.currentReq = requests.get(
                "https://api.openweathermap.org/data/2.5/weather?q=" + self.area + "&appid=" 
                + self.apikey["apitoken"], timeout=5
            )
        except (requests.Timeout, requests.ConnectionError):
            print("No Internet Connection")
    
    def set_data(self):
        """
        Set all data to the DataModel properties
        """
        # read json from the current weather request
        self.current = json.loads(self.currentReq.text)

        self.kelvin = self.current["main"]["temp"]
        self.condition = self.current["weather"][0]["main"]
        self.description = self.current["weather"][0]["description"]
        self.time = self.current["dt"]
        self.icon_id = self.current["weather"][0]["icon"]
