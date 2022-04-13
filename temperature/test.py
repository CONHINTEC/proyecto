import smbus
import time

while True:
	bus = smbus.SMBus(1)
	# SHT31 address, 0x44(68)
#	bus.write_i2c_block_data(0x48, 0x2C, [0x0D]) 
#	time.sleep(0.5)
	 
	# SHT31 address, 0x44(68)
	# Read data back from 0x00(00), 6 bytes
	# Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC
	data = bus.read_i2c_block_data(0x48, 0x00, 6)
 
	# Convert the data
	temp = data[0] * 256 + data[1]
	#formulas deifinidas por el fabricante del sensor
#	cTemp = round(-45 + (175 * temp / 65535.0), 3)
#	humidity = round((100 * (data[3] * 256 + data[4]) / 65535.0),2)
	 
	# Output data to screen
	print("Temperature: ", temp, "°C")
#	print("Humidity   : ", humidity,"%HR")
	time.sleep(1)
