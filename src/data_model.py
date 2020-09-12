from datetime import datetime

class DataModel:
    def __init__(self):
        self.city = None
        self.temp_k = None
        self.weather_condition = None
        self.weather_desc = None
        self.timestamp = None
        self.icon = None

    @property
    def area(self):
        return self.city
    
    @area.setter
    def area(self, value):
        self.city = value
    
    @property
    def kelvin(self):
        return round(self.temp_k, 1)

    @kelvin.setter
    def kelvin(self, value):
        self.temp_k = round(value, 1)

    # No setter needed for celsius
    @property
    def celsius(self):
        return round(self.kelvin - 273.15, 1)
    
    # No setter needed for fahrenheit
    @property
    def fahrenheit(self):
        return round((self.kelvin - 273.15) * 9/5 + 32, 1)

    @property
    def condition(self):
        return self.weather_condition

    @condition.setter
    def condition(self, value):
        self.weather_condition = value

    @property
    def description(self):
        return self.weather_desc.capitalize()

    @description.setter
    def description(self, value):
        self.weather_desc = value

    @property
    def time(self):
        return datetime.utcfromtimestamp(
            self.timestamp
        ).strftime(
            "%Y-%m-%d %H:%M:%S UTC"
        )
    
    @time.setter
    def time(self, value):
        self.timestamp = value

    @property
    def icon_id(self):
        return self.icon
    
    @icon_id.setter
    def icon_id(self, value):
        self.icon = value
