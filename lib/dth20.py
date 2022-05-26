from machine import I2C
from time import sleep_ms

class DHT20(object):
    def __init__(self, i2c):
        self.i2c = i2c
        if (self.status() & 0x80) == 0x80:
            self.init()  
    
    def read(self):
        data = self.read_dht20()
        return self.temperature(data), self.humidity(data)
    
    def read_dht20(self):
        self.i2c.writeto(0x38, bytes([0xac,0x33,0x00]))
        sleep_ms(80)
        cnt = 0
        while (self.status() & 0x80) == 0x80:
            sleep_ms(1)
            if cnt >= 100:
                cnt += 1
                break
        data = self.i2c.readfrom(0x38, 7, True)
        n = []
        for i in data[:]:
            n.append(i)
        return n
        
    def status(self):
        data = self.i2c.readfrom(0x38, 1, True)
        return data[0]
    
    def init(self):
        i2c.writeto(0x38, bytes([0xa8,0x00,0x00]))
        sleep_ms(10)
        i2c.writeto(0x38, bytes([0xbe,0x08,0x00]))
        
    def calc_crc8(self,data):
        crc = 0xff
        for i in data[:-1]:
            crc ^= i
            for j in range(8):
                if crc & 0x80:
                    crc = (crc << 1) ^ 0x31
                else:
                    crc = (crc << 1)
        return crc
    
    def temperature(self, data):
        rawData = ((data[3]&0xf) <<16) + (data[4]<<8)+data[5]
        temperature = float(rawData)/5242 -50
        return temperature
    
    def humidity(self, data):
        rawData = ((data[3]&0xf0) >>4) + (data[1]<<12)+(data[2]<<4)
        humidity = float(rawData)/0x100000
        return humidity*100