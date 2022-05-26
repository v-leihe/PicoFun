import machine
import utime

led_red = machine.Pin(18, machine.Pin.OUT)
led_yellow = machine.Pin(19, machine.Pin.OUT)
led_green = machine.Pin(20, machine.Pin.OUT)

while True:
    led_red.value(1)
    led_yellow.value(0)
    led_green.value(0)

    utime.sleep(2)

    led_red.value(0)
    led_yellow.value(1)
    led_green.value(0)

    utime.sleep(2)

    led_red.value(0)
    led_yellow.value(0)
    led_green.value(1)

    utime.sleep(2)

    led_red.value(1)
    led_yellow.value(1)
    led_green.value(0)

    utime.sleep(2)

    led_red.value(0)
    led_yellow.value(1)
    led_green.value(1)

    utime.sleep(2)

    led_red.value(1)
    led_yellow.value(0)
    led_green.value(1)

    utime.sleep(2)

    led_red.value(1)
    led_yellow.value(1)
    led_green.value(1)

    utime.sleep(2)