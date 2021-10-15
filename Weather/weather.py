import ssd1306
import ujson as json
import urequests as requests
from machine import Pin, SoftI2C

# ESP8266 Pin assignment
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


country_code = "IN"
city = "chennai"

weather_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country_code + "&APPID=b190a0605344cc4f3af08d0dd473dd25"
weather_data = requests.get(weather_url)

#location
location = weather_data.json().get("name") + ", " + weather_data.json().get("sys").get("country")

#weather
weather = "Weather: " + weather_data.json().get("weather")[0].get("main")

#temperature
temperature = (weather_data.json().get("main").get("temp")-273.15)
temp = "Temp: " + str(temperature)+ "C"

#pressure
pressure = "Pressure: "+str(weather_data.json().get("main").get("pressure"))

#wind
wind = "Wind: " + str(weather_data.json().get("wind").get("speed")) + "mps"

#oled commands
oled.text(location, 17, 10, 1)
oled.text(weather, 0, 20, 1)
oled.text(pressure, 0, 30, 1)
oled.text(wind, 0, 40, 1)
oled.text(temp, 0, 50, 1)
oled.show()
