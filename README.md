# JessebotX/Weather App <!-- omit in toc -->
A GUI desktop application to check the current weather forecast.

Made with Python programming language and the built-in Tkinter library.

## Contents <!-- omit in toc -->
- [Install](#install)
    - [Windows](#windows)

## Install
Clone this repository with [git](https://git-scm.com/)
```bash
git clone https://github.com/JessebotX/WeatherApp.git
```

## Usage
- Install [Python](https://www.python.org/)
- To run the app, go to the root directory of the WeatherApp project
```
WeatherApp
|-- README.md (this file)
|-- src/
|---- main.py
|---- ...
```
- then `cd` to the src folder 
```bash
cd src/
```
- Create a `private.json` and paste this in
```json
{
    "apitoken": "{openweathermapapikey}"
}
```
replace {openweathermapapikey} with your api key from [here](https://openweathermap.org/)
- Run `main.py`
```bash
python main.py
```
while you're still in `/WeatherApp/src` folder
