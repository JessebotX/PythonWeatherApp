namespace Jessebot.WeatherApp.Models
{
    public class WeatherModel
    {
        /// <summary> The city that will provide the weather data </summary>
        public string area { get; set; }
        /// <summary> The current temperature in Celsius </summary>
        public float currentTempC { get; set; }
        /// <summary> The current temperature in Fahrenheit </summary>
        public float currentTempF { get; set; }
        /// <summary> The current temperature in Kelvin </summary>
        public float currentTempK { get; set; }
    }
}