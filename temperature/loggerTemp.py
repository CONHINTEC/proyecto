import smbus
import time
import os

try: 
	f = open('/home/cerrejon/Documents/proyect/temperature/data.csv', 'a+')
	if os.stat('/home/cerrejon/Documents/proyect/temperature/data.csv').st_size == 0:
            f.write('Date,Time,Temperature,Humidity\r\n')
except:
	pass


while True:
	bus = smbus.SMBus(1)
	# SHT31 address, 0x44(68)
	bus.write_i2c_block_data(0x44, 0x2C, [0x0D]) 
	time.sleep(0.5)
	 
	# SHT31 address, 0x44(68)
	# Read data back from 0x00(00), 6 bytes
	# Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC
	data = bus.read_i2c_block_data(0x44, 0x00, 6)
 
	# Convert the data
	temp = data[0] * 256 + data[1]
	#formulas deifinidas por el fabricante del sensor
	cTemp = round(-45 + (175 * temp / 65535.0), 3)
	humidity = round((100 * (data[3] * 256 + data[4]) / 65535.0),2)
	 
	# Output data to screen
	print("Temperature: ", cTemp, "°C")
	print("Humidity   : ", humidity,"%HR")
	f.write('{0},{1},{2}°C,{3}%HR\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), cTemp, humidity))
#	f.write(Date,Time,cTemp,humidity)
	time.sleep(1)
