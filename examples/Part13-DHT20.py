from machine import I2C
import utime
from dht20 import DHT20

# Init I2C using I2C0 defaults, SCL=Pin(GP9), SDA=Pin(GP8), freq=400000
sensor = DHT20(I2C(0))

while True:
    temperature, humidity = sensor.read()
    print("Temperature: {}°C   Humidity: {:.0f}% ".format(temperature, humidity))
    utime.sleep_ms(2000)

