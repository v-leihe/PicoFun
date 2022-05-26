from machine import Pin
import utime
from dht11 import DHT11, InvalidChecksum
 
sensor = DHT11(Pin(16, Pin.OUT, Pin.PULL_DOWN))
 
while True:
    print("Temperature: {}°C   Humidity: {:.0f}% ".format(sensor.temperature, sensor.humidity))
    utime.sleep_ms(2000)